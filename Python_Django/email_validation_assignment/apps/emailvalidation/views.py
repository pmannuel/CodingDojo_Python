from django.shortcuts import render, redirect, HttpResponse
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

        print ('*'*70)
        print request.session['flash']['isvalid']
        print ('*'*70)

        if request.session['flash']['isvalid']:
            print ('*'*70)
            print "email is registered"
            Users.validate.create(
                email = email
            )
            print Users.validate.all()
            print ('*'*70)

    return redirect('/')
