from django.urls import path
from my_project import views 
from . import views




urlpatterns = [
    # path('', views.index, name='index'),
    path('update_form/', views.updateform, name='updateform'),
    path('restaurant_add/', views.add_restaurant, name='add_restaurant'),    


    path('add_rating/', views.add_rating, name='add_rating'),
    path('create_student', views.create_student, name='create_student'),

    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
    #bootstrap sample

    path('bootstrap_buttons/', views.bootstrap_buttons, name='bootstrap_buttons'),
    
    path('bootstrap_utility_classes/', views.bootstrap_utility_classes, name='bootstrap_utility_classes'),
    path('containers/', views.containers, name='containers'),
    path('grid/', views.grid, name='grid'),
    path('grid_layout/', views.grid_layout, 
         name='grid_layout'),
    path('cards/', views.cards, name='cards'),         
]
