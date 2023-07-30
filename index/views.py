# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Person

def index(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})

def update_person(request):
    if request.method == 'POST':
        person_id = request.POST.get('id')
        name = request.POST.get('name')
        adress = request.POST.get('adress')
        age = request.POST.get('age')

        try:
            person = get_object_or_404(Person, pk=person_id)
            person.name = name
            person.adress = adress
            person.age = age
            person.save()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'Error updating person data.'})

    return HttpResponseBadRequest('Invalid request')
