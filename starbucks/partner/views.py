from django.shortcuts import render

# Create your views here.
def partner(request):
    return render(request, 'partner/partner.html')

def management(request):
    return render(request, 'partner/management.html')

def baristas(request):
    return render(request, 'partner/baristas.html')

def potq(request):
    return render(request, 'partner/potq.html')

def coffee_master(request):
    return render(request, 'partner/coffee_master.html')

