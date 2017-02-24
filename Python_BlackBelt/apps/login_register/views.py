from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Users, UsersManager

def index(request):
    # Users.objects.all().delete()
    print ('*'*100)
    print Users.objects.all()
    print ('*'*100)

    return render(request, 'login_register/index.html')

def logout(request):
    del request.session['active_user_id']
    return redirect(reverse('login_register:index'))

def login(request):
    if request.method == "POST":
        chk_username = request.POST['username']
        chk_password = request.POST['password']

        if Users.objects.filter(username = chk_username).exists():
            user_active = Users.objects.get(username = chk_username)
            passwordMatch = Users.objects.check_password_match(chk_password, user_active.password)
            if passwordMatch:
                request.session['active_user_id'] = user_active.id
                return redirect(reverse('main:index'))
            else:
                messages.error(request,'Incorrect password')
        else:
            messages.error(request,'Email does not exist')

    return redirect(reverse('login_register:index'))

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        error_messages = Users.objects.register(firstname, lastname, username, email, password, cpassword)

        if error_messages == []:
            diffpassword = Users.objects.encrypt(password)
            Users.objects.create(
                firstname = firstname,
                lastname = lastname,
                username = username,
                email = email,
                password = diffpassword
            )
            user_active = Users.objects.get(email = email)
            request.session['active_user_id'] = user_active.id
            return redirect(reverse('main:index'))
        else:
            for i in range(0, len(error_messages)):
                messages.error(request, error_messages[i])

    return redirect(reverse('login_register:index'))
