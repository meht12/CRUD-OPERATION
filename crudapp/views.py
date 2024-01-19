from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from crudapp.models import *
# home
def home(request):

    return render(request,'crudapp/home.html')
# base
def base(request):
    return render (request,'crudapp/base.html')
# view record in forms.py class name is create record 
@login_required(login_url='/login')
def view_record(request,pk):
    single_record=record.objects.get(id=pk)
    return render(request, 'crudapp/view-record.html', {'record':single_record})
    # dashboard
@login_required(login_url='/login')
def dashboard(request):
    data=record.objects.all()
    return render(request,'crudapp/dashboard.html',{'record':data})
  # login
def login(request):
    form=Login()
    if request.method=="POST":
        form=Login(request.POST,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/dashboard')
    return render(request, 'crudapp/login.html',{'form':form})
# register
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login',{"your account created succcessfully"})
    context = {'form': form}
    return render(request, 'crudapp/register.html', context)
    
# update record
@login_required(login_url='/login')
def update_record(request,pk):
    records=record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method=='POST':
        form = UpdateRecordForm(request.POST,instance=request)
        if form.is_valid:
            form.save()
        return redirect('/dashboard')
    return render(request, 'crudapp/update-record.html',{'record':records},{'form':form})
# Create record
@login_required(login_url='/login')
def create_record(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=int(request.POST.get('phone'))
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        a=record()
        a.name=name
        a.email=email
        a.phone=phone
        a.address=address
        a.city=city
        a.state=state
        a.country=country
        a.creation_date
        a.save()
        return redirect('/dashboard')
    return render(request,'crudapp/create-record.html',)

# User_logout
def user_logout(request):
    auth.logout(request)
    return redirect('/login')

# read and view a singular record

@login_required(login_url='login')
def update_record(request,pk):
    all_record=record.objects.get(id=pk)
    all_record.save()
    return render(request,'crudapp/update-record.html' ,{'record':all_record})

@login_required(login_url='login')
def delete(request,pk):
    datas=record.objects.get(id=pk)
    datas.delete()
    return redirect('/dashboard' ,{'record':datas})