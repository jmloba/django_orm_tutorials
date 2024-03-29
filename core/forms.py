from django import forms
from django.forms import ModelForm
from .models import Rating , Restaurant, Stud_file



# from django.core.validators import MinValueValidator, MaxValueValidator



class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ('restaurant','user','rating')



class RestaurantForm(forms.ModelForm) :
  class Meta:
    model = Restaurant
    fields = ('name','website','date_opened',"latitude", "longitude","restaurant_type")

class  Stud_fileForm(ModelForm) :
  class Meta:
    model = Stud_file
    fields=('studno','firstname', 'lastname','birthdate')
    labels ={
      'studno': 'Student Number',
      'firstname':'First Name',
      'lastname': 'Last Name',
      'birthdate': 'Birth Date'
    }
    widgets={
      'studno': forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Student Number'} ),
      'firstname': forms.TextInput(attrs={ 'class':'form-control', 'placeholder' :'First Name' }),
      'lastname': forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'lastname' } ),
      'birthdate': forms.DateInput(attrs={ 'class':'form-control', 'placeholder':'Birthday'} )

    }

    # fields = '__all__'


