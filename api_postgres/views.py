from django.shortcuts import render
from rest_framework import viewsets
from .serializers import reports_serializer
from .models import reports

class reports_viewset(viewsets.ModelViewSet):
    queryset=reports.objects.all()
    serializer_class = reports_serializer


# Create your views here.
def home(request):
    context = {'reports': reports}
    return render(request, 'base/home.html', context)