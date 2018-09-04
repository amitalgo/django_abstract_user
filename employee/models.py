from django.contrib.auth.models import AbstractUser
from django.db import models
from branch.models import Branch
from django.conf import settings

# Create your models here.
class MyUser(AbstractUser):
    college = models.CharField(null=True,blank=True,max_length=40)
    pass

class UserBranch(models.Model):
    branch = models.ForeignKey(Branch,null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.branch.branch_name