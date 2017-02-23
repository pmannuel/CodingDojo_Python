from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Users, UsersManager, Books, Authors, Reviews

def index(request):
    user_id = request.session.get('active_user_id')
    recent_reviews = Books.objects.all().order_by('-created_at')[:3]
    data = {
        "user" : Users.objects.get(id=user_id),
        "recent_reviews" : recent_reviews,
        "other_reviews" : Books.objects.all()
    }
    return render(request, 'main/index.html', data)
