# metrics/views.py
from rest_framework import viewsets
from .models import PRDetails, DeploymentDetails
from .serializers import PRDetailsSerializer, DeploymentDetailsSerializer

class PRDetailsViewSet(viewsets.ModelViewSet):
    queryset = PRDetails.objects.all()
    serializer_class = PRDetailsSerializer

class DeploymentDetailsViewSet(viewsets.ModelViewSet):
    queryset = DeploymentDetails.objects.all()
    serializer_class = DeploymentDetailsSerializer
