from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ExpenseInfo
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    expense_items = ExpenseInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    return render(request,'budget_app/index.html',{'expense_items':expense_items})

def add_item(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    print(name,expense_cost,expense_date)
    ExpenseInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    return HttpResponseRedirect('app')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
