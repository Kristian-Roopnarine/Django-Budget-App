from django.db import models

# Create your models here.

class AccountInfo(models.Model):
    username = models.CharField(max_length=20)
    password =models.CharField(max_length=20)

class BudgetInfo(models.Model):
    user_budget = models.IntegerField()
    expenses = models.IntegerField()
    category = models.CharField(max_length=10)
