from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Users, UsersManager, TripsManager, Trips, Joins
from django.contrib import messages
from datetime import datetime

def index(request):
    # Joins.objects.all().delete()
    # Trips.objects.all().delete()
    # Users.objects.all().delete()

    user_id = request.session.get('active_user_id')
    other_trips = Trips.objects.all()

    for other_trip in other_trips:
        other_trip.activeUserPlanned = False
        other_trip.save()
        if other_trip.user_id == user_id:
            other_trip.activeUserPlanned = True
            other_trip.save()

    data = {
        "user" : Users.objects.get(id=user_id),
        "trips" : Trips.objects.all(),
        "join_trips": Joins.objects.filter(joining_user__id=user_id),
        "other_trips" : Trips.objects.all()
        }
    return render(request, 'main/index.html', data)

def add(request):
    if request.method == "POST":
        user_id = request.session.get('active_user_id')

        #data from form
        destination = request.POST['destination']
        description = request.POST['description']
        travel_date_from = request.POST['travel_date_from']
        travel_date_to = request.POST['travel_date_to']
        present = str(datetime.now().date())

        error_messages = Trips.objects.validate(present, destination, description, travel_date_from, travel_date_to)

        if error_messages == []:
            Trips.objects.create(
                destination = request.POST['destination'],
                description = request.POST['description'],
                travel_date_from = request.POST['travel_date_from'],
                travel_date_to = request.POST['travel_date_to'],
                user = Users.objects.get(id=user_id),
            )
            return redirect(reverse('main:index'))
        else: #HAVE error messages
            for i in range(0, len(error_messages)):
                messages.error(request, error_messages[i])
            return render(request, 'main/add.html')

    else: #request.method is NOT "POST"
        return render(request, 'main/add.html')

def trip_info(request, trip_id):
    data = {
        "trips" : Trips.objects.get(id=trip_id),
        "joining_users" : Joins.objects.filter(trip__id=trip_id)
        }
    return render(request, 'main/trip_info.html', data)

def join(request, trip_id):
    user_id = request.session.get('active_user_id')
    Joins.objects.create(
        trip = Trips.objects.get(id=trip_id),
        joining_user = Users.objects.get(id=user_id),
    )
    return redirect(reverse('main:trip_info', kwargs={'trip_id': trip_id}))
