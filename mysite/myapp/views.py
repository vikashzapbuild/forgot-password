from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from .form import LoginForm
from django.http import HttpResponse


def login_user(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)

        if form.is_valid():
            cd= form.cleaned_data
            user=authenticate(request,
                             username=cd['username'],
                             password=cd['password'])



        if user is not None:
            login(request,user)
            return HttpResponse('Authentication is successful')
        else:
            return HttpResponse("aUTHENTICATION IS FAILED PLEASE TRY AGAIN")
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
