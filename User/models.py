from django.db import models

# Create your models here.
class Data(models.Model):
    grade=models.CharField(max_length=10)
    laptop=models.CharField(max_length=10)
    shift=models.CharField(max_length=20)
    time=models.TimeField()
    parentname=models.CharField(max_length=100)
    stuname=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=10)
    email=models.EmailField()


class Dbt(models.Model):
    question=models.CharField(max_length=200,default=None)
    file=models.FileField(default=None)


