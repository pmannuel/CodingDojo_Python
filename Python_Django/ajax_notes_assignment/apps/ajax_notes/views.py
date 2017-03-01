from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import View
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Notes

def index(request):
	return render(request, 'ajax_notes/index.html')

class add_note(View):
    def get(self, request):
        data = {
            'notes' : Notes.objects.all()
        }
        return render(request, 'ajax_notes/ajax.html', data)

    def post(self, request):
        Notes.objects.create(
                title = request.POST['title'],
                content = request.POST['content']
            )
        return redirect(reverse('ajax_notes:add_note'))

def edit(request):
    edit = Notes.objects.get(id = request.POST['edit_form_id'])
    edit.title = request.POST['title']
    edit.content = request.POST['content']
    edit.save()
    return JsonResponse(model_to_dict(note))

class delete_note(View):
    def get(self, request):
        return redirect(reverse('ajax_notes:add_note'))

    def post(self, request):
        note = Notes.objects.get(id = request.POST['id']).delete()
        return redirect(reverse('ajax_notes:delete_note'))
