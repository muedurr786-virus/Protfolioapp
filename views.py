from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *


def registerpage(req):
    if req.method == 'POST':
        form = UserModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    
    form = UserModelForm()
    contex ={
        'form':form,
        'form_titel': 'Register page',
        'btn' : 'Register'
    }
    return render(req,'auth/baseForm.html',contex)

def loginpage(req):
    if req.method == 'POST':
        form = AuthForm(req,req.POST)
        if form.is_valid():
            user=form.get_user()
            login(req,user)
            return redirect('dashboard') 
    
    form = AuthForm()
    contex ={
        'form':form,
        'form_titel': 'Login page',
        'btn' : 'Login'
    }
    return render(req,'auth/baseForm.html',contex)

def logoutpage(req):
    logout(req)
    return redirect('login')

@login_required
def personalinfo_page(req):
    try:
        info = PersonalInfoModel.objects.get(user=req.user)
    except PersonalInfoModel.DoesNotExist:
        info = PersonalInfoModel.objects.create(user=req.user)

    if req.method == 'POST':
        form = PersonalInfoModelForm(req.POST, req.FILES, instance=info)
        if form.is_valid():
            form.save()
            messages.success(req,"Personal Info Page  Create successful.")
            return redirect('dashboard')
    else:
        form = PersonalInfoModelForm(instance=info)

    context = {
        'form': form,
        'form_titel': 'Personal Information',
        'btn': 'Submit'
    }
    return render(req, 'baseform.html', context)

@login_required
def project_page(req):


    if req.method == 'POST':
        form = ProjectModelForm(req.POST, req.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(req,"Project Page  Create successful.")
            return redirect('dashboard')
    else:
        form = ProjectModelForm()

    context = {
        'form': form,
        'form_titel': 'Project Page',
        'btn': 'Submit'
    }
    return render(req, 'baseform.html', context)

@login_required
def technical_page(req):


    if req.method == 'POST':
        form = TechnicalModelForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Technical Page  Create successful.")
            return redirect('dashboard')
    else:
        form = TechnicalModelForm()

    context = {
        'form': form,
        'form_titel': 'Technical Skills',
        'btn': 'Submit'
    }
    return render(req, 'baseform.html', context)

@login_required
def experience_page(req):

    if req.method == 'POST':
        form = ExprinceModelForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Exprince Page  Create successful.")
            return redirect('dashboard')
    else:
        form = ExprinceModelForm()

    context = {
        'form': form,
        'form_titel': 'Experience',
        'btn': 'Submit'
    }
    return render(req, 'baseform.html', context)

@login_required
def education_page(req):

    if req.method == 'POST':
        form = EducationModelForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Educational Page  Create successful.")
            return redirect('dashboard')
    else:
        form = EducationModelForm()

    context = {
        'form': form,
        'form_titel': 'Education',
        'btn': 'Submit'
    }
    return render(req, 'baseform.html', context)

@login_required
def dashboardPage(req):
    try:
        info = PersonalInfoModel.objects.get(id=1)
    except PersonalInfoModel.DoesNotExist:
        return HttpResponse("Personal info not found.")

        
    work = ExprinceModel.objects.all()
    edu = EducationModel.objects.all()
    project = ProjectModel.objects.all()
    technical = TechnicalModel.objects.all()

    context = {
        'info':info,
        'work':work,
        'edu':edu,
        'projects':project,
        'technical':technical,
    }
    return render(req,'dashboard.html',context)
