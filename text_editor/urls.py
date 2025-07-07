from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_text/', views.save_text, name='save_text'),
    path('show_data/', views.show_data, name='show_data'),
]