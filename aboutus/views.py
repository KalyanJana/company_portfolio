from django.shortcuts import render
from .models import AboutUs

def all_aboutus(request):
    aboutuses=AboutUs.objects.all()
    return render(request, 'aboutus/all_aboutus.html', {'aboutuses':aboutuses})
