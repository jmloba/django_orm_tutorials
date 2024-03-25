from django.db import models

# Restaurant
# user
# Rating

class Restaurant(models.Model):
  name = models.CharField(max_length=100, unique = True)
  website=models.URLField(default='')
  date_opened= models.DateField()
  latitude = models.FloatField()
  longitude = models.FloatField()
  def __str__(self) :
    return self.name
  


