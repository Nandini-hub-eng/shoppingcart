"""shoppingcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import cartview
from . import indexview
from . import contactusview
from . import productview
from . import signupview



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexview.displayindex),
    path('signup',signupview.displaysignup, name="displaysignup"),
    path('signup',signupview.insertsignup,name="insertsignup"),
    path('contactus',contactusview.displaycontactus,name="displaycontactus"),
    path('contactus',contactusview.insertcontactus,name="insertcontactus"),
path('product',productview.displayproduct,name="displayproduct"),
path('buycart',cartview.displaybuycart,name="displaybuycart"),
    path('buycart',cartview.insertbuycart,name="insertbuycart")
]
