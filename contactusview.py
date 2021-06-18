from django.shortcuts import render
from shoppingcart.contactusmodel import contactusmodel
from django.contrib import messages

def displaycontactus(request):
    return render(request, 'contactus.html')

def insertcontactus(request):
    if request.method == "POST":
        if request.POST.get('fullname') and request.POST.get('email') and request.POST.get('password'):
            saverecord = contactusmodel()
            saverecord.fullname = request.POST.get('fullname')
            saverecord.email = request.POST.get('email')
            saverecord.message= request.POST.get('message')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully..!')
            return render(request, 'contactus.html')
    else:
            return render(request, 'contactus.html')