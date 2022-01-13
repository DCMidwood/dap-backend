from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('civil_mto/', views.return_civmto)
]
