"""toystudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from community import views
from account import views as account_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first,name='first'),
    path('login/',account_views.login,name='login'),
    path('logout/',account_views.logout,name='logout'),
    path('signup/',account_views.signup, name='signup'),
    path('again_signup/',account_views.again_signup, name='again_signup'),
    path('test/', account_views.test, name='test'),
    path('plus_test/', account_views.plus_test, name='plus_test'),
    path('mult_test/', account_views.mult_test, name='mult_test'),
    path('minus_test/', account_views.minus_test, name='minus_test'),
    path('div_test/', account_views.div_test, name='div_test'),
]
