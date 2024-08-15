# metrics/models.py
from django.db import models

class PRDetails(models.Model):
    project_name = models.CharField(max_length=100)
    repo_name = models.CharField(max_length=100)
    pr_number = models.IntegerField()
    from_branch = models.CharField(max_length=100)
    to_branch = models.CharField(max_length=100)
    merged_at = models.DateTimeField()
    merged_by = models.CharField(max_length=100)

class DeploymentDetails(models.Model):
    project_name = models.CharField(max_length=100)
    repo_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    deployment_status = models.CharField(max_length=100)
    deployed_at = models.DateTimeField()
    deployment_by = models.CharField(max_length=100)
