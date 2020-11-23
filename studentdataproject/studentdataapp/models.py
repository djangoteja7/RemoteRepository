from django.db import models

# Create your models here.
class StudentData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    company=models.CharField(max_length=100)
    salary=models.IntegerField()
    location=models.CharField(max_length=100)