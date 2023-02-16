
from django.db import models

# Create your models here.
class contact(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=100)
    Phone=models.TextField()
    Message=models.TextField()
