from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import MedicineForm
from .models import MedicineModel
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    # return HttpResponse("Signup Page")
    if request.method == 'POST':
        Username = request.POST.get('username')
        Email = request.POST.get('email')
        Password = request.POST.get('pw1')
        password_confirmation = request.POST.get('pw2')

        if Password == password_confirmation:
            myuser = User.objects.create_user(Username,Email,Password)
            myuser.save()
            return redirect('log')
        else:
            return HttpResponse("Password Mismatch")
        
    return render(request,'medicine/signup.html')

def log(request):
    # return HttpResponse("Login Page")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pw1')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            # return render(request,'medicine/medicList.html')4
            return redirect('medicList')
        else:
            return HttpResponse("Invalid Credentials")
        
    return render(request,'medicine/signin.html')

@login_required(login_url='/signup/')
def medList(request):
    
    context = {'medicList':MedicineModel.objects.all()}

    return render(request,'medicine/medicList.html',context)

@login_required(login_url='/signup/')
def medDelete(request,id):
    
    med = MedicineModel.objects.get(pk=id)
    med.delete()
    return redirect('medicList')



@login_required(login_url='/signup/')
def medView(request,id):
    med = MedicineModel.objects.get(pk=id)
    return render(request,'medicine/medicView.html',{'med':med})

@login_required(login_url='/signup/')
def medEdit(request,id):
    
    if request.method == 'GET':

        med = MedicineModel.objects.get(pk=id)
        form = MedicineForm(instance=med)
        return render(request,'medicine/medicEdit.html',{'form':form})

    else:
        med = MedicineModel.objects.get(pk=id)
        form = MedicineForm(request.POST,instance=med)
        if form.is_valid():
            form.save()
            return redirect('medicList')

@login_required(login_url='/')
def medCreate(request):
    if request.method == 'GET':
        form = MedicineForm()

    else:
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicList')
    return render(request,'medicine/medicCreate.html',{'form':form})

def logout_view(request):
        logout(request)
        return redirect('log')