from django.shortcuts import render, redirect
import random, math, datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if (('logs' in request.session) == False):
        request.session['logs'] = []

    return render(request,'ninjagold/index.html')

def reset(request):
    del request.session['gold']
    del request.session['logs']

    return redirect('/')

def process_money(request, activity):
    txt_color = "green" #initialize log text color to green

    if activity == 'farm':
        earning = random.randint(10,20)
    if activity == 'cave':
        earning = random.randint(5,10)
    if activity == 'house':
        earning = random.randint(2,5)
    if activity == 'casino':
        earning = random.randint(-50,50)
        if earning < 0:
            txt_color = "red"

    #Register activity log
    timestamp = '{:(%Y/%m/%d %H:%M%p)}'.format(datetime.datetime.now())
    log = "Earned {} from the {}! ".format(earning, activity) + timestamp
    log_data = {
        'act_log' : log,
        'txt_color' : txt_color
    }
    request.session['logs'].insert(0, log_data) #append front

    # Update gold status accordingly
    request.session['gold'] += earning

    return redirect('/')
