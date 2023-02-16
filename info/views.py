from django.shortcuts import render,redirect
from django.contrib import messages
from .models import contact

# Create your views here.
def portfolio(request):

    #data fetch
    if request.method=="POST":
        name = request.POST.get("name")
        email =request.POST.get("email")
        phone =request.POST.get("phone")
        message =request.POST.get("message")
        #create model object and set the data
        c= contact()
        c.Name=name
        c.Email=email
        c.Phone=phone
        c.Message=message
        #save the object
        c.save()
        messages.success(request,"Data is successfully added")
        # return redirect('home')
        return render(request, 'index.html',{'name':name})
    return render(request, 'index.html')
    

