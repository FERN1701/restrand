
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from restrand.decorators import role_required
from django.core.paginator import Paginator
from .forms import *
from datetime import datetime
from django.utils.timezone import now 
import pytz
from django.db.models import Sum, Max
from twilio.rest import Client
from django.http import JsonResponse



def home(request):
    usecount = User.objects.filter(is_superuser=0).count()
    if usecount == 0:
         return redirect('createaacount')
    system_details = get_object_or_404(setting_detail, id=1)
    list_team = team_detail.objects.all()
    main = 1
    context = {
        'main':main,
        'system_details':system_details,
        'list_team':list_team
    
    }
    return render(request,'index.html',context)

def recommend(request):
    main = 0
    context = {
        'main':main
    }
    return render(request,'recommend_menu.html',context)

def form1(request):
    main = 0
    context = {
        'main':main
    }
    return render(request,'recommend.html',context)


def form2(request):
    main = 0
    context = {
        'main':main
    }
    return render(request,'recommend_2.html',context)


def result(request):
    main = 0
    context = {
        'main':main
    }
    return render(request,'result.html',context)

def check_subjects(request):
    main = 0
    context = {
        'main':main
    }
    return render(request,'check_subjects.html',context)

def pre_search(request):
    main = 0
    context = {
        'main':main
    }
    return render(request,'pre_search.html',context)



#=============================================================================
#Administrative 



def signin(request):
    
    page = 'login'
    if request.user.is_authenticated:
        
        return redirect('administrator')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Account does not exist')
            return render(request, 'public/signin.html', {'page': page})

        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Check user's status and code
            if user.status == 'verified' or user.code == 0:
                login(request, user)
                messages.success(request,'Login succesfully')
                return redirect('administrator')
            else:
                # Save email in session and render a template for email verification
                request.session['unverified_email'] = email
                messages.success(request,'Please Verify your Account')
                return render(request, 'admin/verify.html', {'user': user})
        else:
            messages.error(request, 'please try again')

    context = {
        'page': page,
        }
    return render(request,'admin/login.html')


def exit_account(request):
    user = request.user
    user.log_status = "offline"
    user.save()
    logout(request)
    return redirect('home')

def createaacount(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            request.session['unverified_email'] =  user.email
            user.code = int(get_random_string(length=6, allowed_chars='1234567890'))
            user.save()
            subject = 'Account Verification'
            message = f'Your OTP is {user.code}. Enter this code to complete your registration.'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = user.email
            try:
                send_mail(subject, message, from_email, [to_email], fail_silently=False)
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # for Direct log in after registration
            messages.success(request, 'Account Created Successfully')
            return redirect('verify_email')
        else:
            messages.error(request, 'An error occurred during registration {form.errors}')
    
    context = {
        'form': form,
    }
    return render(request,'admin/register.html',context)




def verify_email(request):
    if request.method == 'POST':
        otp = request.POST.get("otp")
        email = request.session['unverified_email']

        if not email:
            messages.error(request, 'Email not found in session')
            return redirect('signin')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User not found')
            return redirect('signin')

        # Perform pattern match on user code
        if str(user.code) == otp:
            user.status = "verified"
            user.code = 0  # Assuming 0 represents the verified status
            user.save()
            messages.info(request, 'Account verified and signed in successfully...')
            subject = 'Account Verification'
            message = f'Congratulations! Your account is now verified. You can now log in. '
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = user.email
            send_mail(subject, message, from_email, [to_email], fail_silently=False)
            request.session.flush()
            messages.success(request, "Account Verified")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('administrator')
        else:
            messages.error(request, "Code doesn't match")

    return render(request, 'admin/verify.html')


def resetpassword(request):
    main = 0
    context = {
        'main':main
    }
    return render(request,'admin/forgot.html',context)


def renewpassword(request):
    main = 0
    context = {
        'main':main
    }
    return render(request,'admin/renew_password.html',context)




@login_required(login_url='signin')
def administrator(request):
    users = request.user
   
    context = {
        
    }
    return render(request, 'admin/dashboard.html',context)



@login_required(login_url='signin')
def settings(request):
    users = request.user
    list_team = team_detail.objects.all()
    system_details = get_object_or_404(setting_detail, id=1)
    if request.method == 'POST':
        form = system_form(request.POST, request.FILES, instance=system_details)
        
        if form.is_valid():
            details = form.save(commit=False) 
            details.save()  
            messages.success(request, "Updated Successfully")
            return redirect('settings')
        form2 = team_forms(request.POST, request.FILES)
        if form2.is_valid():
            teams = form2.save(commit=False) 
            teams.save()  
            messages.success(request, "Added Successfully")
            return redirect('settings')
        else:
            print(form2.errors)  # Debug form errors
            messages.error(request, "Please Try Again")
    else:
        form = system_form(instance=system_details)
        form2 = team_forms()
    context = {
        'form':form,
        'form2':form2,
        'list_team':list_team,
        
    }
    return render(request, 'admin/settings.html',context)



@login_required(login_url='signin')
def delete_team(request, pk):
    shop_del = get_object_or_404(team_detail, id=pk)
    shop_del.delete()
    messages.success(request, " Deleted successfully")
    return redirect('settings')
