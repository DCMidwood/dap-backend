from rest_framework import serializers
from .models import reports

class reports_serializer(serializers.ModelSerializer):
    class Meta:
        model = reports 
        fields = '__all__'