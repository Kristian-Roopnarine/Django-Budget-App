from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request,'budget_app/index.html')
'''
def login(request):
    return render(request,'budget_app/login.html')

def check_info(request):
    return HttpResponseRedirect('app')
'''