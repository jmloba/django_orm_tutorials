from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.core.validators import MinValueValidator,MaxValueValidator
# Restaurant
# user
# Rating
def validate_restaurant_name_begins_with_letter_a(value):
  if not value.startswith('a'):
    raise ValidationError('Name must begin with letter "a"')

class Restaurant(models.Model):
  class TypeChoices(models.TextChoices):
    INDIAN = 'IN','Indian'
    CHINESE ='CH','Chinese'
    PILIPPINE='PH','Filipino'
    OTHER='OT','Others'

  name = models.CharField(max_length=100, 
                          unique = True,
                          validators=[validate_restaurant_name_begins_with_letter_a]
                          )
  website=models.URLField(default='')
  date_opened= models.DateField()
  latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
  longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
  restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
  def __str__(self) :
    return self.name
  
  def save(self,*args, **kwargs):
    print(self._state.adding)
    super().save(*args, **kwargs)


  
class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  rating = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)]
  )
  def __str__(self) :
    return  str(self.rating)
  
class Sale(models.Model)  :
  restaurant= models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales' )
  income = models.DecimalField(decimal_places=2, max_digits=8)
  datetime =models.DateTimeField()

class Stud_file(models.Model) :
  studno = models.CharField(max_length=8)
  firstname = models.CharField(max_length=30) 
  lastname = models.CharField(max_length=30) 
  birthdate = models.DateField()
  def __str__(self):
    return f'{self.firstname} {self.lastname}'



class Courses(models.Model) :
  course_code =models.CharField(max_length= 8)
  course_desc= models.CharField(max_length=100)

  def __str__(self):
    return f'{course_code} {course_code}'

