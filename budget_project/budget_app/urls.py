from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('app',views.index,name='index'),
    path('check_info',views.check_info,name="check_info")
]