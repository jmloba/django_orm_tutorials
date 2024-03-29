from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Rating, Restaurant, Stud_file

from .forms import RatingForm ,RestaurantForm, Stud_fileForm
from django.http import JsonResponse


# Create your views here.



def updateform(request):
  # restaurants = Restaurant.objects.first()
  restaurants = Restaurant.objects.first()
  print(restaurants)
  restaurants.name = 'New resto -updte'
  restaurants.save()
  context = {'restaurants': restaurants}
  return redirect('index')


def restaurant_list1(request):
  # restaurants = Restaurant.objects.first()
  restaurants = Restaurant.objects.all()
  print(restaurants)
  context = {'restaurants': restaurants}
  return render(request,'core/restaurant_list.html', context)

def restaurant_list(request):
  restaurants = Restaurant.objects.all()
  context={'restaurants':restaurants}
  return render(request,'core/restaurant_list.html', context)
  


def add_rating(request):
  rating = Rating.objects.all()
  if request.method=='POST':
    form= RatingForm(request.POST or None)
    if form.is_valid():
      print(form.cleaned_data)
      form.save()

      return redirect('add_rating')
    else:
      return render(request,'core/add_rating.html',{'form':form})
 
  context={'form': RatingForm(),'rating':rating }
  return render(request,'core/add_rating.html',context)

def add_restaurant(request):
  if request.method =='POST':

    form = RestaurantForm(request.POST or None)
    if form.is_valid():
      print(form.cleaned_data)
      form.save()
      return redirect('index')
    
    else :
      return render(request, 'core/add_restaurant.html', {'form': form})

  context  = {'form': RestaurantForm(),}
  return render(request,'core/add_restaurant.html', context )

def create_student(request):
  submitted = False
  students = Stud_file.objects.all()
  if request.method=='POST':
    form = Stud_fileForm(request.POST or None)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/create_student?submitted=True')
    
    # else: 
    #   context = {'form': form, 'students': students}
    #   return render(request, 'core/create_student.html',context)

  else:  
    form = Stud_fileForm
    if 'submitted' in request.GET:
      submitted = True
  context = {'form': form, 'students': students, 'submitted':submitted}
  return render(request,'core/create_student.html', context)

def bootstrap_buttons(request):
  return render(request,'core/bootstrap/buttons.html' )

def bootstrap_utility_classes(request):
  return render(request,'core/bootstrap/utility_classes.html' )

def containers(request):
  return render(request,'core/bootstrap/containers.html' )

def grid(request):
  return render(request,'core/bootstrap/grid.html' )

def grid_layout(request):
  return render(request,'core/bootstrap/grid_layout.html' )
def cards(request):
  return render(request,'core/bootstrap/cards.html' )