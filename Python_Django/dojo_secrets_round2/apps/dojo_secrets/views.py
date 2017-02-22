from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Users, Validator, Secrets, Likes
from django.db.models import Count, Case, Value, When
import datetime

def index(request):
    # Secrets.objects.all().delete()
    # Likes.objects.all().delete()
    user_id = request.session.get('active_user_id')

    secrets = Secrets.objects.all().annotate(num_likes=Count('secret_liked'))

    #option 1
    for secret in secrets:
        secret.isLiked = False
        secret.save()
        if Likes.objects.filter(user_liked_id=user_id, liked_secrets_id=secret.id).exists():
            print "here"
            print secret
            secret.isLiked = True
            secret.save()

    for secret in secrets:
        print secret.isLiked

    # secrets = secrets.annotate(Likes.objects.filter(user_liked_id=user_id, liked_secrets_id=self.id).exists())

    #option 2
    # secrets = secrets.annotate(
    #     alreadyLiked=Case(
    #         When(Likes.objects.filter(user_liked_id=user_id, liked_secrets_id=self.id).exists(), then=Value('True')),
    #         default=Value('False')
    #     )
    # )

    #option 3
    # secrets = secrets.annotate(
    #     alreadyLiked=Case(
    #         When(hasattr(liked_secrets, user_id), then=Value(True)),
    #         default=Value(False)
    #     )
    # )

    #option 4
    # secrets = secrets.annotate(
    #     alreadyLiked=Case(
    #         When(user_liking=user_id, then=Value('True')),
    #         default=Value('False')
    #     )
    # )

    data = {
        "user" : Users.validate.get(id=user_id),
        "secrets" : secrets
    }
    return render(request, 'dojo_secrets/index.html', data)

def addsecret(request):
    if request.method == "POST":
        Secrets.objects.create(
            user = Users.validate.get(id=request.POST['creator']),
            content = request.POST['secret'],
            created_at = '{:(%Y/%m/%d %H:%M%p)}'.format(datetime.datetime.now())
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

def delete(request, id):
    secret_id = id
    Secrets.objects.get(id=secret_id).delete()

    return redirect(reverse('dojo_secrets:index'))

def mostpopular(request):
    popular = {
        "secrets" : Secrets.objects.annotate(num_likes=Count('secret_liked')).order_by('-num_likes')[:5]
    }
    return render(request, 'dojo_secrets/mostpopular.html', popular)
