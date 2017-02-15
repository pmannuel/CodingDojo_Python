from django.shortcuts import render, redirect

def index(request):
    return render(request,'survey_form/index.html')

def result(request):
    if request.method == "POST":

        if ('sess_active' in request.session):
            del request.session['sess_active']
            del request.session['name']
            del request.session['dojolocation']
            del request.session['favlanguage']
            del request.session['comment']

        request.session['sess_active'] = request.POST['sess_active']
        request.session['name'] = request.POST['name']
        request.session['dojolocation'] = request.POST['dojolocation']
        request.session['favlanguage'] = request.POST['favlanguage']
        request.session['comment'] = request.POST['comment']

    return render(request,'survey_form/result.html')
