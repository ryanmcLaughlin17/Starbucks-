from django.shortcuts import render
from .models import Review

# Create your views here.
def favourites(request):
    review = Review.objects.all()
    return render(request, 'favourites/favourites.html', {'review':review})
