from django.shortcuts import render

def index(request):
    flag = {
        "noNinjas" : True
    }
    return render(request, 'disappearingninjas/index.html', flag)

def show_ninjas(request):
    flag = {
        "allNinjas" : True
    }
    return render(request, 'disappearingninjas/index.html', flag)

def show_the_ninja(request, color):
    flag = {
        "allNinjas" : False,
        "color" : color
    }
    return render(request, 'disappearingninjas/index.html', flag)
