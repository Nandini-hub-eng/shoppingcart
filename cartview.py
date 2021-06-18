from django.shortcuts import render
from shoppingcart.cartmodel import cartmodel
from django.contrib import messages

def displaybuycart(request):
    return render(request, 'buycart.html')

def insertbuycart(request):
    if request.method == "POST":
        if request.POST.get('userid') and request.POST.get('productid') and request.POST.get('qty'):
            saverecord = cartmodel()
            saverecord.userid = request.POST.get('userid')
            saverecord.productid = request.POST.get('productid')
            saverecord.qty= request.POST.get('qty')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully..!')
            return render(request, 'buycart.html')
    else:
            return render(request, 'buycart.html')