
from  core.models import Restaurant, Rating, Sale
from django.utils import timezone

from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def add_data_restaurant():
  print('--->>> hello from runscript')
  r = Restaurant()
  r.name = 'Resto abc'
  r.websute =''
  r.date_opened= timezone.now()
  r.latitude = 14.1820
  r.longitude=120.8880
  r.restaurant_type=r.TypeChoices.PILIPPINE
  r.save()

def get_restaurant_data_all():
  restautants = Restaurant.objects.all()
  for restaurant  in restautants:
    print(restaurant.name)

def get_restaurant_data_filter():
  restautants = Restaurant.objects.filter(name='resto a')
  if restautants:
    for restaurant  in restautants:
      print(f'restaurant name : {restaurant.name}')    
      print(connection.queries)
  else:
      print(' *** no data from restaurant obtained')    

def get_restaurant_per_index():   
  # restaurant=Restaurant.objects.all()[1]   
  restaurant=Restaurant.objects.all()
 
  
  # print(f'restaurant : {restaurant.name}, latitude : {restaurant.latitude}')
  print(restaurant)
  print(f'resto count : {restaurant.count()}')
  print(connection.queries)

def create_model_insert():
  Restaurant.objects.create(
    name='Resto 25', 
    date_opened= timezone.now(),
    latitude=14.1960, 
    longitude =120.8778,
    restaurant_type= Restaurant.TypeChoices.INDIAN
  )
  print(connection.queries)

def CreateRating_foreignkey():
  resto = Restaurant.objects.first()
  user = User.objects.first()
  print(resto)

  Rating.objects.create(user=user, restaurant= resto, rating = 4)

def Filter_Records():
  rating_obj = Rating.objects.filter(rating =  4)
  print(rating_obj)


  rating_obj = Rating.objects.filter(rating__gte = 3)
  print(rating_obj)  
  print(connection.queries)
  rating_obj = Rating.objects.filter(rating__lte = 3)
  print(rating_obj)  
  print(connection.queries)

def   exlude_filter():
  rating_obj = Rating.objects.exclude(rating =  3  )
  print(rating_obj)
  print(connection.queries)

def edit_values(): 
  rating = Rating.objects.first()
  print(f'resto name : {rating.restaurant.name}, date opened : {rating.restaurant.date_opened}')
  # print(resto.name)
  # resto.name='resto joven--ab '
  # resto.save()
  pprint(connection.queries)


def backward_relationship():  
  resto = Restaurant.objects.first()
  print(resto.rating_set.all)
  pprint(connection.queries)

def with_related_name(): 
  Sale.objects.create(
    restaurant = Restaurant.objects.first(),
    income=28.23,
    datetime=timezone.now()
  )
  Sale.objects.create(
    restaurant = Restaurant.objects.last(),
    income=14.23,
    datetime=timezone.now()
  )
def create_data_rating():  
  user = User.objects.first()
  restaurant = Restaurant.objects.first()
  # note : if record exist it will not create a new record with values rating = 6
  rating,create= Rating.objects.get_or_create(
        restaurant= restaurant,
        user=user,
        rating=6
      ) 
  pprint(connection.queries)

def field_validators_1():
  user = User.objects.first()
  restaurant =Restaurant.objects.first()
  # Rating.objects.create(user=user,restaurant=restaurant, rating= 9)
  rating = Rating(user=user,restaurant=restaurant, rating= 9)
  rating.full_clean()
  rating.save()

  pprint(connection.queries)

def update_restaurant():
  restaurant = Restaurant.objects.first()
  print(f'restaurant.name is : {restaurant.name}')
  restaurant.name  = 'joven resto 1'
  restaurant.save(update_fields=['name'])
  print(f'restaurant.name is : {restaurant.name}')
  pprint(connection.queries)

def add_restaurant(): 
  restaurant = Restaurant() 
  restaurant.name ='My Italian restaurant 2'
  restaurant.date_opened = timezone.now()
  restaurant.restaurant_type= Restaurant.TypeChoices.CHINESE
  restaurant.latitude=20.5
  restaurant.longitude= 160.5
  restaurant.save()
  pprint(connection.queries)

def update_query_set (): 
  # restaurants = Restaurant.objects.filter(name='Resto 25')
  # restaurants.update(    date_opened = timezone.now()  )
  # print(connection.queries)

  # restaurants = Restaurant.objects.exclude(name='Resto 25')
  # restaurants.update(    latitude = 25.66  )
  # print(connection.queries)
  
  restaurants = Restaurant.objects.filter(name__startswith='R')
  print(restaurants)
  print(restaurants.update(
    latitude= 19, 
    date_opened =timezone.now() - timezone.timedelta(days=45),
    website='www.test.com'
    ))
  
  print(connection.queries)

def delete_query_sets()  :
  print('joven')
  restaurant = Restaurant.objects.first()
  print(restaurant.pk)
  print(restaurant.ratings.all())

  

def run():
  # get_restaurant_data_filter()
  # get_restaurant_per_index()  
  # create_model_insert() 
  # CreateRating_foreignkey()
  # Filter_Records()
  # exlude_filter()
  # edit_values()
  # backward_relationship()
  # with_related_name()
  # create_data_rating()

  '''model fields validators'''
  # field_validators_1()

  '''model updating table'''
  # update_restaurant()
  # add_restaurant()
  # update_query_set()
  delete_query_sets()





  



  