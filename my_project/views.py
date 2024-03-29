from core.models import Rating, Restaurant
from core.forms import RatingForm, RestaurantForm
from django.shortcuts import render, HttpResponse,redirect

def index(request):
 
  return render(request,'main_project/index.html',  )
