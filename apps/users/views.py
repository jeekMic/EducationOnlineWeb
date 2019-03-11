from django.shortcuts import render
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_pwd = request.POST.get("password")
        # print("user_name:  ", user_name)
        # print("user_pwd:  ", user_pwd)
        # user = auth.authenticate(username=user_name, password=user_pwd)
        # if user is not None:
        #     auth.login(request, user)
        #     return render(request, 'login.html', {})
        # else:
        #     return "ERROR"
        return "ERROR"
    elif request.method == "GET":
        user_name = "admin"
        pass_word  = "123"

        return render(request, 'login.html', {})
