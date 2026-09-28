from django.db import models

# Create your models here.
class student(models.Model):
    std_id=models.IntegerField(unique=True)
    std_name=models.CharField(max_length=20)
    std_age=models.IntegerField()
    email=models.EmailField(unique=True)
    Mobile=models.BigIntegerField(unique=True)
    
    
