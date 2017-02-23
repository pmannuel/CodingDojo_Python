from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Users, UsersManager, Books, Authors, Reviews
from django.db.models import Count

def index(request):
    # Reviews.objects.all().delete()
    # Books.objects.all().delete()
    # Authors.objects.all().delete()
    user_id = request.session.get('active_user_id')
    recent_reviews = Reviews.objects.all().order_by('-created_at')[:3]
    recent_reviews_ids = []
    other_books = Books.objects.all()

    for review in recent_reviews:
        recent_reviews_ids.append(review.id)

    print recent_reviews_ids[1]

    for other_book in other_books:
        other_book.isRecent = False
        for i in range(0, 3):
            if Reviews.objects.filter(id=recent_reviews_ids[i], book__id=other_book.id).exists():
                other_book.isRecent = True
                other_book.save()

    data = {
        "user" : Users.objects.get(id=user_id),
        "recent_reviews" : recent_reviews,
        "other_reviews" : Books.objects.all()
    }
    return render(request, 'main/index.html', data)

def user(request, user_id):
    data = {
        "users" : Users.objects.filter(id=user_id).annotate(num_reviews=Count('posted_reviews')),
        "reviews_by_user" : Reviews.objects.filter(user__id=user_id)
    }
    return render(request, 'main/userpage.html', data)

def book(request, book_id):
    user_id = request.session.get('active_user_id')
    data = {
        "active_user" : Users.objects.get(id=user_id),
        "book" : Books.objects.get(id=book_id),
        "author" : Authors.objects.get(books__id=book_id),
        "reviews" : Reviews.objects.filter(book__id=book_id)
    }
    return render(request, 'main/bookpage.html', data)

def del_review(request, review_id):
    Reviews.objects.filter(id=review_id).delete()
    return redirect(reverse('main:index')) #TBE: redirect to respective bookpage

def add_review(request, book_id):
    if request.method == "POST":
        this_book = Books.objects.get(id=book_id)
        user_id = request.session.get('active_user_id')

        Reviews.objects.create(
            content = request.POST['review'],
            rating = int(request.POST['rating']),
            user = Users.objects.get(id=user_id),
            book = this_book
        )
    return redirect(reverse('main:index'))
