from datetime import datetime
from rest_framework import serializers
from .models import Client, Service

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('full_name', 'phone', 'service', 'date')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'description', )