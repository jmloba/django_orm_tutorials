from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Restaurant, Rating, Sale, Stud_file, Courses

# Register your models here.

class RestaurantUserAdmin(UserAdmin):
  list_display=('name','website','date_opened','latitude','longitude','restaurant_type')
  ordering=('name',)

  filter_horizontal =()
  list_filter =()
  fieldsets=()

class RatingUserAdmin(UserAdmin):  
  list_display=('restaurant', 'user', 'rating')
  ordering=('restaurant',)
  filter_horizontal =()
  list_filter =()
  fieldsets=()

class StudfileUserAdmin(UserAdmin):  
  list_display=('studno', 'firstname', 'lastname','birthdate')
  ordering=('studno',)
  
  filter_horizontal =()
  list_filter =()
  fieldsets=()

    
class CourseUserAdmin(UserAdmin):  
  list_display=('course_code', 'course_desc',)
  ordering=('course_code',)

  filter_horizontal =()
  list_filter =()
  fieldsets=()


admin.site.register(Restaurant,RestaurantUserAdmin)
admin.site.register(Rating, RatingUserAdmin)
admin.site.register(Sale)
admin.site.register(Stud_file,StudfileUserAdmin)
admin.site.register(Courses,CourseUserAdmin)