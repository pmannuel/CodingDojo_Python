from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Courses, Users, User_Courses
from django.db.models import Count

def index(request):
    data = {
        "users" : Users.validate.all(),
        "results" : Courses.objects.all().annotate(num_users=Count('course_e'))
    }

    return render(request, 'integration/index.html', data)

def add_user_to_course(request):
    if request.method == "POST":
        user_id = request.POST['user_selected']
        course_id = request.POST['course_selected']

        this_user = Users.validate.get(id=user_id)
        this_course = Courses.objects.get(id=course_id)

    User_Courses.objects.create(
        course_id = this_course,
        user_id = this_user
    )

    return redirect(reverse('main:main_index'))
