from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(),name='login'),
    path('app',views.index,name='index'),
    path('add_item',views.add_item,name='add item'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout',views.logout_view,name='logout'),
    path('sign_up',views.sign_up,name="sign up")
]