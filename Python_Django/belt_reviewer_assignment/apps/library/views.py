from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Books, Authors, Reviews, Users, UsersManager

def index(request):
    # Books.objects.all().delete()
    # Authors.objects.all().delete()
    data = {
        "books" : Books.objects.all(),
        "authors" : Authors.objects.all()
    }
    return render(request, 'library/index.html', data)

def add(request):
    if request.method == "POST":
        book_title = request.POST['book']

        author_name = request.POST['author']
        if author_name == '':
            author_name = request.POST['select_author']

        Books.objects.create(
            title = book_title
        )

        if not Authors.objects.filter(name=author_name).exists():
            Authors.objects.create(
                name = author_name
            )

        this_book = Books.objects.get(title=book_title)
        this_author = Authors.objects.get(name=author_name)
        this_author.books.add(this_book)

        user_id = request.session.get('active_user_id')

        Reviews.objects.create(
            content = request.POST['review'],
            rating = int(request.POST['rating']),
            user = Users.objects.get(id=user_id),
            book = this_book
        )

        print '****************************'
        print Books.objects.all()
        print Authors.objects.all()
        print '****************************'
    return redirect(reverse('main:index'))
