from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    context = {
    "date": '{:%B %d, %Y}'.format(datetime.datetime.now()),
    "time": '{:%H:%M %p}'.format(datetime.datetime.now())
    }
    return render(request,'timedisplay/page.html', context)
