import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class staffInfo(models.Model):
    name = models.CharField(max_length=20, null=True)
    sex = models.CharField(max_length=6, null=True)
    age = models.IntegerField(null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("staff:detail", args=[str(self.id)])
    
class User(models.Model):
    userName = models.CharField(max_length=20, null=False)
    def __str__(self) -> str:
        return self.userName
    email = models.EmailField(max_length=50, null=False)
    def __str__(self) -> str:
        return self.email
    password = models.CharField(max_length=8, null=False)
    def __str__(self) -> str:
        return self.password
    isActive = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.isActive