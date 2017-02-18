from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Users

def index(request):
    data = {
        "users" : Users.validate.all()
    }
    return render(request, 'emailvalidation/index.html', data)

def validate(request):
    if request.method == "POST":
        email = request.POST['email']
        request.session['flash'] = Users.validate.register(email)

        print ('~'*70)
        print request.session['flash']['isvalid']
        print ('~'*70)

        if request.session['flash']['isvalid']:

            Users.validate.create(
                email = email
            )
            messages.success(request, 'FLASH WORKS')
            messages.success(request, 'FLASH: your email is valid!')

            sigh = messages
            print ('*'*70)
            print messages
            print sigh
            print ('*'*70)

    return redirect('/')
