from django.db import models

# Create your models here.

class AccountInfo(models.Model):
    username_ = models.CharField(max=20)
    password_=models.CharField(max=20)

class BudgetInfo(models.Model):
    user_budget = models.IntegerField()
    expenses = models.IntegerField()
    category = models.CharField(max=10)
