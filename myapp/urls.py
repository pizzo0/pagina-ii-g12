from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('medidor/', views.app, name="app"),
  path('mas_sobre_el_proyecto/', views.about, name="about")
]