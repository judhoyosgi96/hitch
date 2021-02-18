from django.db import models

class Dataset(models.Model):
    """Dataset class"""
    Name = models.CharField(max_length=50, null=False)
    Team = models.CharField(max_length=50, null=False)
    Number = models.IntegerField(null=True)
    Position = models.CharField(max_length=10, null=False)
    Age = models.IntegerField(null=True)
    Height = models.DateField(null=False)
    Weight = models.IntegerField(null=True)
    College = models.CharField(max_length=50, null=False)
    Salary = models.CharField(max_length=50, null=True)
