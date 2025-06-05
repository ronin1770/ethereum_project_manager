from django.db import models
from django.utils import timezone


class Project(models.Model):
    project_name = models.CharField(max_length=255, default='Untitled Project')
    customer_id = models.IntegerField(default=0)
    project_description = models.TextField(default='No description provided.')
    project_start = models.DateTimeField(default=timezone.now)
    project_end = models.DateTimeField(default=timezone.now)
    project_actual_start = models.DateTimeField(default=timezone.now)
    project_actual_end = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    project_manager_id = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_name


class Sprint(models.Model):
    project_id = models.IntegerField(default=0)
    customer_id = models.IntegerField(default=0)
    project_manager_id = models.IntegerField(default=0)
    sprint_start = models.DateTimeField(default=timezone.now)
    sprint_end = models.DateTimeField(default=timezone.now)
    sprint_description = models.TextField(default='No description provided.')
    estimated_hours = models.IntegerField(default=0)
    total_items = models.IntegerField(default=0)
    total_completed = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Sprint {self.id} - Project {self.project_id}"
