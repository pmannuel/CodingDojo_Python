from django.shortcuts import render, redirect
import datetime

def index(request):
    if not ('courses' in request.session):
        request.session['courses'] = []

    return render(request,'courses/index.html')

def add_course(request):
    if request.method == "POST":
        a_course_data = {
            'name' : request.POST['course_name'],
            'description' : request.POST['description'],
            'created_at' : '{:%B/%d/%Y, %H:%M %p}'.format(datetime.datetime.now())
        }

    request.session['courses'].insert(0,a_course_data)
    request.session['necessary'] = 'idontknowwhy'

    print ('*'*50)
    print request.session['courses']
    print ('*'*50)

    return redirect('/')


def rem_course(request, course_id):

    return redirect('/')
