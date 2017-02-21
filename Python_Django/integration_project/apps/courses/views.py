from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Courses
import datetime

def index(request):
    data = {
        "courses": Courses.objects.all()
    }
    return render(request,'courses/index.html', data)

def add_course(request):
    if request.method == "POST":

        Courses.objects.create(
            name = request.POST['course_name'],
            description = request.POST['description'],
        )
    return redirect(reverse('courses:courses_index'))


def rem_course(request, course_id):
    Courses.objects.filter(id = course_id).delete()
    return redirect(reverse('courses:courses_index'))
