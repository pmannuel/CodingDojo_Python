from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import friend, friendship

def index(request):
    context= {
        "friends": friend.objects.all(),
        "friendships": friendship.objects.all()
    }
    return render(request, 'friend/index.html', context)

def create(request):
    if request.method=='POST':
        friend.objects.create(name=request.POST['friend'])
    return redirect(reverse('friend:index'))

def join(request):
    if request.method=='POST':
        # form = YourForm(request.POST)
        # if form.is_valid():
        #     answer = form.cleaned_data['value']
        friend1_id = request.POST['friend1']
        friend2_id = request.POST['friend2']

        this_friend1 = friend.objects.get(id=friend1_id)
        this_friend2 = friend.objects.get(id=friend2_id)

        friendship.objects.create(friend1 = this_friend1, friend2 = this_friend2)

    return redirect(reverse('friend:index'))
