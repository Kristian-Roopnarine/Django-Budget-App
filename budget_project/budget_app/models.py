from django.db import models
from django.utils import timezone

# Create your models here.

class AccountInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_budget = models.IntegerField()
    
    def __str__(self):
        return self.username

class ExpenseInfo(models.Model):
    expense_name = models.CharField(max_length=20)
    cost = models.IntegerField()
    date_added = models.DateTimeField()
    user = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)