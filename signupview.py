from django.shortcuts import render
from shoppingcart.signupmodel import signupmodel
from django.contrib import messages
from django.http import HttpResponse

def displaysignup(request):
    return render(request, 'signup.html')

def insertsignup(request):
    if request.method == "POST":
        if request.POST.get('fullname') and request.POST.get('email') and request.POST.get('password'):
            saverecord = signupmodel()
            saverecord.fullname = request.POST.get('fullname')
            saverecord.email = request.POST.get('email')
            saverecord.password= request.POST.get('password')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully..!')
            return render(request, 'signup.html')
    else:
            return render(request, 'signup.html')


