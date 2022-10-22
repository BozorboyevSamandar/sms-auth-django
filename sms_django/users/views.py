from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from random import randint
from django.contrib import messages
from .models import User
from twilio.rest import Client


# Create your views here.

def send_sms(body, number):
    account_sid = 'aa'
    auth_token = 'ss'
    client = Client(account_sid, auth_token)
    message = client.message.create(
        body=body,
        form='test_text',
        to=number,
    )


def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            confirm = user.confirm = randint(10000, 99999)
            user.save()
            # send sms
            send_sms("You activation code is " + str(confirm), user.phone)
            return redirect('confirm', user.id)
            messages.warning(request, 'success')
        else:
            messages.warning(request, 'Wrong details, please try again')
            return redirect('/login')

    return render(request, 'login.html')


def confirm(request, id):
    if not request.user.is_authenticated:
        user = User.objects.get(id=id)
        if user and user.confirm != 0:
            if request.method == 'POST':
                confirm = request.POST['confirm']
                if user.confirm == int(confirm):
                    login(request, user)
                    user.confirm = 0
                    user.save()
                else:
                    messages.warning(request, 'Wrong!!!')
        else:
            return redirect('/')
    else:
        return redirect('/')
    return render(request, 'confirm.html', {'user': user})
