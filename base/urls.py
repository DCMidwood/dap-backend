from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('report/<str:pk>/',views.report, name="report")
]