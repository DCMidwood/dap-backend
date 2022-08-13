from posixpath import basename
from django.urls import path
from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
# from .views import turbine_list, report_list
from api import views

# router = SimpleRouter()
# router.register('turbine_list', turbine_list, basename="")
# router.register('report_list', report_list, basename="")

# urlpatterns = router.urls
urlpatterns = [
    path('turbine_list/',views.turbine_list),
    path('report_list/', views.report_list),
    path('zip/', views.download_zip)
]