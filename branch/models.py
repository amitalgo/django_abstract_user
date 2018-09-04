from django.db import models
from django.conf import settings

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(null=True, blank=True, max_length=40)
    def __str__(self):
        return self.branch_name