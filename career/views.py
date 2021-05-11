from django.shortcuts import render
from .models import Career

def all_career(request):
    careers =Career.objects.all()
    return render(request, 'career/all_career.html', {'careers':careers})
