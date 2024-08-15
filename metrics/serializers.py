# metrics/serializers.py
from rest_framework import serializers
from .models import PRDetails, DeploymentDetails

class PRDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRDetails
        fields = '__all__'

class DeploymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeploymentDetails
        fields = '__all__'
