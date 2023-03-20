from django.shortcuts import render
from .models import Barista, Manager
# Create your views here.
def partner(request):
    return render(request, 'partner/partner.html')

def management(request):
     manager = Manager.objects.all()
     return render(request, 'partner/management.html', {'manager':manager})

def barista(request):
    barista = Barista.objects.all().order_by('name')
    return render(request, 'partner/barista.html', {'barista':barista})

def potq(request):
    return render(request, 'partner/potq.html')

def coffee_master(request):
    return render(request, 'partner/coffee_master.html')


