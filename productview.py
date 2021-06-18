from django.shortcuts import render
from shoppingcart.productmodel import productmodel
from django.contrib import messages

def displayproduct(request):
    return render(request,'product.html')

