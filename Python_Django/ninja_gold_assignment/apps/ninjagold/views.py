from django.shortcuts import render, redirect
import random, math, datetime

def index(request):
    if (('gold' in request.session) == False):
        request.session['gold'] = 0
    if (('logs' in request.session) == False):
        request.session['logs'] = []

    return render(request,'ninjagold/index.html')

def reset(request):
    del request.session['gold']
    del request.session['logs']

    return redirect('/')

def process_money(request, activity):
    action = activity
    txt_color = "green" #initialize log text color to green

    # register location
    if action != 'reset':
        location = activity

    if action == 'farm':
        earning = random.randint(10,20)
    if action == 'cave':
        earning = random.randint(5,10)
    if action == 'house':
        earning = random.randint(2,5)
    if action == 'casino':
        earning = random.randint(-50,50)
        if earning < 0:
            txt_color = "red"

    #Register activity log
    timestamp = '{:(%Y/%m/%d %H:%M%p)}'.format(datetime.datetime.now())
    log = "Earned {} from the {}! ".format(earning, location) + timestamp
    log_data = {
        'act_log' : log,
        'txt_color' : txt_color
    }
    request.session['logs'].append(log_data)

    # Update gold status accordingly
    request.session['gold'] += earning

    return redirect('/')
