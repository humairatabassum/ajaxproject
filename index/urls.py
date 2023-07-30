# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_person/', views.update_person, name='update_person'),
]
