from django.shortcuts import render,HttpResponseRedirect
from . models import pizza_type
from . forms import pizza_data,signup
from  django.contrib import  messages
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def home(request):
            pd = pizza_type.objects.all()
            return render(request,'home.html',{'pizzadata':pd})



def delet_pizza(request,id):
    if request.method == 'POST':
        pd = pizza_type.objects.get(pk=id)
        pd.delete()
        messages.warning(request,"deleted successfull")
    return HttpResponseRedirect('/')

def update_pizza(request,id):
    if request.method == 'POST':
        pi = pizza_type.objects.get(pk=id)
        fm = pizza_data(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Update successgully..........")
            return HttpResponseRedirect('/')
    else:
        ide = pizza_type.objects.get(pk=id)
        fm = pizza_data(instance=ide)

    return render(request, 'updatepizza.html', {'form': fm})

def user_singup(request):
    if request.method == "POST":
        fm = signup(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sing up successfully")
            return HttpResponseRedirect('/singin')
    else:
        fm = signup()
        return render(request,'singup.html',{'form':fm})

def user_singin(request):
    if request.method == "POST":
        uname = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=uname,password=password)
        if user:
            login(request,user)
            messages.success(request, "log in successfully.......")
            return  HttpResponseRedirect('/')
        else:
            messages.warning(request, "something is wrong......")
            return render(request, 'singin.html')
    else:

        return render(request,'singin.html')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_chek(request):
     if request.method == 'POST':
        fm = pizza_data(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"adding successgully..........")
            fm = pizza_data()
            return render(request,'editpizza.html',{'form':fm})

     else:
         fm = pizza_data()
         return render(request,'editpizza.html',{'form':fm})