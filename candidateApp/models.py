from time import timezone
from django.db import models

# Create your models here.
from django.db import models


STATUS_CHOICES = (
    ("Accepted" , "Accepted"),
    ("Rejected" , "Rejected"),
    ("Applied" , "Applied")
)

class candidateModel(models.Model):
    name = models.CharField(max_length=50 )
    email = models.CharField(max_length=50 , null=True)
    phone = models.CharField( max_length=10)
    education = models.CharField(max_length=50)
    experience = models.CharField(max_length=500)
    status = models.CharField(max_length=8 , choices=STATUS_CHOICES , default='Applied')
    applied_on = models.DateField(auto_now_add=True , editable=False)