from django.shortcuts import render, redirect
import datetime, random, string

def index(request):
    context = {
    "date": '{:%B %d, %Y}'.format(datetime.datetime.now()),
    "time": '{:%H:%M %p}'.format(datetime.datetime.now())
    }
    return render(request,'timedisplay/page.html', context)

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def create_user(request):
    if request.method == "POST":
        print ('*'*50)
        print request.POST
        print request.POST['email']

        if ('word' in request.session):
            del request.session['word']

        print ('word' in request.session)
        print ('*'*50)

        request.session['word'] = randomword(10)
    return redirect('/')
