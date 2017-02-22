from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

#############################################

def index(request):
        return render(request, 'logreg/index.html')

def login(request):
    if request.method == "POST":
        chk_email = request.POST['email']
        chk_password = request.POST['password']

        try:
            user_active = Users.validate.get(email = chk_email)
            passwordMatch = Users.validate.check_password_match(chk_password, user_active.password)
            if passwordMatch:
                print "success"
                messages.success(request, 'HELLO THERE {}! You are logged in.'.format(user_active.firstname))
            else:
                messages.error(request,'Incorrect password')
        except:
            messages.error(request,'Email does not exist')

    return redirect(reverse('logreg:index'))

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        error_messages = Users.validate.register(firstname, lastname, email, password, cpassword)

        if error_messages == []:
            messages.success(request, 'You are officially part of the club!')
            Users.validate.create(
                firstname = firstname,
                lastname = lastname,
                email = email,
                password = Users.validate.encrypt(password)
            )
        else:
            for i in range(0, len(error_messages)):
                messages.error(request, error_messages[i])

    return redirect(reverse('logreg:index'))
