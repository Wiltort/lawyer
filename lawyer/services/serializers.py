from datetime import datetime
from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('full_name', 'phone', 'service', 'date')
