from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome {username} your account is register')
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,'register.html',{'form':form})

@login_required
def profilePage(request):
    return render(request,'profile.html')
