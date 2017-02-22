from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Users, Validator, Secrets, Likes
from django.db.models import Count
import datetime

def index(request):
    # Secrets.objects.all().delete()
    # Likes.objects.all().delete()

    user_id = request.session.get('active_user_id')
    data = {
        "user" : Users.validate.get(id=user_id),
        "secrets" : Secrets.objects.all().annotate(num_likes=Count('secret_liked'))
    }
    return render(request, 'dojo_secrets/index.html', data)

def addsecret(request):
    if request.method == "POST":
        Secrets.objects.create(
            content = request.POST['secret'],
            created_at = '{:(%Y/%m/%d %H:%M%p)}'.format(datetime.datetime.now()),
            # author = request.POST['creator'],
        )
    return redirect(reverse('dojo_secrets:index'))

def like(request, id):
    secret_id = id
    user_id = request.session.get('active_user_id')

    this_user = Users.validate.get(id=user_id)
    this_secret = Secrets.objects.get(id=secret_id)

    Likes.objects.create(
        user_liked = this_user,
        liked_secrets = this_secret
    )

    return redirect(reverse('dojo_secrets:index'))
