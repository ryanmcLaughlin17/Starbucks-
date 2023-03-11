from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "catalogue/home.html")

def partners(request):
    return render(request, "team/partners.html")

