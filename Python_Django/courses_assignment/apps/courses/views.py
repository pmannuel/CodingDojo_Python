from django.shortcuts import render, redirect
from .models import Courses
import datetime

data = {
    "courses": Courses.objects.all()
}

def index(request):
    return render(request,'courses/index.html', data)

def add_course(request):
    if request.method == "POST":

        Courses.objects.create(
            name = request.POST['course_name'],
            description = request.POST['description'],
        )

    return redirect('/')


def rem_course(request, course_id):
    Courses.objects.filter(id = course_id).delete()
    return redirect('/')
