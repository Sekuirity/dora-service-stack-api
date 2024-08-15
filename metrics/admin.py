from django.contrib import admin
from .models import PRDetails, DeploymentDetails

admin.site.register(PRDetails)
admin.site.register(DeploymentDetails)

