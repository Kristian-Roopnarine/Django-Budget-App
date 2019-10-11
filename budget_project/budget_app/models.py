from django.db import models

# Create your models here.

class AccountInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class BudgetInfo(models.Model):
    user_budget = models.IntegerField()
    expenses = models.IntegerField()
    user = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)