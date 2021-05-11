from django.shortcuts import render
from .models import EnvironmentsAndHealthSafety

def all_aboutEnvironmentandhealthsafety(request):
    allenvironments=EnvironmentsAndHealthSafety.objects.all()
    return render(request, 'Environment/environmentsAndHealthSafety.html', {'allenvironments':allenvironments})
