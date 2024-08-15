# metrics/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PRDetailsViewSet, DeploymentDetailsViewSet

router = DefaultRouter()
router.register(r'pr_details', PRDetailsViewSet)
router.register(r'deployment_details', DeploymentDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
