from django.shortcuts import render
from shoppingcart.indexmodel import indexmodel
from django.contrib import messages

def displayindex(request):
    return render(request,'index.html')