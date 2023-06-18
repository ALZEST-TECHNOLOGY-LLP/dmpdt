from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
import time
import uuid
from django.core.mail import *
from django.template.loader import *
from django.utils.html import *
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def user_login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/account/login')

    else:
        print('user exits')

    return render(request, 'login.html')


# def user_signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['fname']
#         last_name = request.POST['lname']
#         username = request.POST['uname']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']
#
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Taken')
#                 print('user exits')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Taken')
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email,
#                                                 first_name=first_name, last_name=last_name)
#                 user.save();
#                 messages.success(request, 'user created')
#                 print('user created')
#                 send_info_email(request=request, email=email, username=username)
#                 return redirect('/account/login/')
#
#         else:
#             messages.info(request, 'password not matching..')
#     return render(request, 'signup.html')


def logout_v(request):
    logout(request)
    return redirect('/account/login/')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('/account/login/')
    else:
        username = request.user.username
        if request.method == 'POST':
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                u = User.objects.get(username__exact=username)
                u.set_password(password1)
                u.save()
                messages.success(request, 'password changed')
                logout(request)
                return redirect('/account/login/')
            else:
                messages.error(request, 'password not matching..')
                return redirect('/account/changepassword/')

    return render(request, 'changepass.html')


def reset_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        userch = User.objects.get(username__exact=username)

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'username not exists')
            return redirect('/account/resetpassword/')

        else:
            usera = User.objects.get(username__exact=username)
            if user_pass_token.objects.filter(user=usera.id).exists():

                passtoken = user_pass_token.objects.get(user=usera.id)
                pass_email(request=request, email=usera.email, token=passtoken.pass_token)
            else:
                userid = User.objects.get(id=usera.id)
                token = str(uuid.uuid4())
                tokenpass = user_pass_token.objects.create(user=userid, user_email=usera.email, pass_token=token)
                # tokenpass.user_name=username
                # tokenpass.user_email=email
                # tokenpass.user_id=user.id
                # tokenpass.token=token
                tokenpass.save()
                pass_email(request=request, email=usera.email, token=token)

    return render(request, 'forgotpassword.html')


def chbyempassword(request, token):
    if user_pass_token.objects.filter(pass_token=token).exists():
        forgetpasstoken = user_pass_token.objects.get(pass_token=token)
        context = {'user': forgetpasstoken, 'token': forgetpasstoken.pass_token}
        return render(request, 'chbyempass.html', context)

    else:
        messages.error(request, "Token not Found Please Again try")
        return redirect('/account/resetpassword/')


def pass_reset_done(request):
    if request.method == 'POST':
        user = request.POST['user']
        token = request.POST['token']
        forgetpasstoken = user_pass_token.objects.get(pass_token=token)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            u = User.objects.get(username__exact=user)
            u.set_password(password1)
            u.save()
            messages.success(request, 'password changed')
            forgetpasstoken.delete()
            return redirect('/account/login/')
        else:
            messages.error(request, 'password not matching..')
            return chbyempassword(request, token)


# def pass_email(request,email,token):
#     html_temp = 'email_template.html'
#     context = {'token' : token}
#     email_data = get_template(html_temp).render(context)
#     mailr = email
#     subject= 'Your Forgotten Password Reset Mail From Rakshak Uvc Robot'
#     email_msg = mail.EmailMessage(subject,email_data,settings.EMAIL_HOST_USER, [mailr] )
#     email_msg.context_subtype = 'html'
#     email_msg.send(fail_silently=False)
#     messages.success(request,'Email Sent To Your Rigistered Email Address')
#     return redirect('/useraccount/resetpassword/')


def pass_email(request, email, token):
    context = {'token': token}
    html_temp = render_to_string("email_template-reset-pass.html", context)
    text_temp = strip_tags(html_temp)
    mailr = email
    subject = 'Your Forgotten Password Reset Mail From Rakshak Uvc Robot'
    email_data = EmailMultiAlternatives(subject, text_temp, settings.EMAIL_HOST_USER, [mailr])
    email_data.attach_alternative(html_temp, "text/html")
    email_data.send(fail_silently=False)
    messages.success(request, 'Email Sent To Your Rigistered Email Address')
    return redirect('/account/resetpassword/')


def send_info_email(request, email, username):
    context = {'email': email, 'username': username}
    html_temp = render_to_string("info_mail.html", context)
    text_temp = strip_tags(html_temp)
    mailr = email
    subject = 'Welcome Mail From Rakshak Disinfactant Robot'
    email_data = EmailMultiAlternatives(subject, text_temp, settings.EMAIL_HOST_USER, [mailr])
    email_data.attach_alternative(html_temp, "text/html")
    email_data.send(fail_silently=False)