from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import *
from django.shortcuts import render_to_response, redirect
from uzytkownicy.forms import RegisterForm, EditProfileForm, UserForm

def login(request):
    c = {}
    c.update(csrf(request))
    if request.method =='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)    
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            print username
            auth.login(request, user)
        # Redirect to a success page.        
            return HttpResponseRedirect("/uzytkownik/")
        else:
        # Show an error page
            return HttpResponseRedirect("/blad-logowania/")
    else:
        return render_to_response('uzytkownicy/login.html',c) 

def user_view(request):
    print 'user-site'
    return render_to_response('uzytkownicy/user.html', locals())

def profile_view(request):
    print 'profile'
    user = request.user.get_profile()
    return render_to_response('uzytkownicy/profile.html', locals())

def blad_logowania(request):    
    return render_to_response('uzytkownicy/blad.html', locals())        

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')

def register_view(request):
    def errorHandle(error, account_form):
        return render_to_response('uztkownicy/register.html'), {
                                                                'error' : error,
                                                                'account_form' : account_form
                                                                }
    if request.user.is_authenticated():
        return HttpResponseRedirect('/uzytkownik/')
    else:
        if request.method == 'POST':
            account_form = RegisterForm(request.POST)
            if account_form.is_valid():
                username = account_form.cleaned_data['username']
                email = account_form.cleaned_data['email']
                password = account_form.cleaned_data['password']
                new_user = User.objects.create_user(username, email, password)
                new_user.is_active = True 
                new_user.save()
                account = account_form.save(commit=False)
                account.user = new_user                                
                account.save()
                return HttpResponseRedirect('/loguj/')
            else:
                error = u'Form is invalid'
                return errorHandle(error,account_form)
        else:
            account_form = RegisterForm()
            return render_to_response('uzytkownicy/register.html', {
                                                                'account_form':
                                                                account_form
                                                                })
                                 
def edit_profile_view(request):
    def errorHandle(error, account_form):
        return render_to_response('uztkownicy/register.html'), {
                                                                'error' : error,
                                                                'account_form' : account_form
                                                                }
    account = request.user.get_profile()
    if request.method == 'POST':
        account_form = EditProfileForm(request.POST, instance = account)        
        if account_form.is_valid():                               
                account_form.save()
                return render_to_response('uzytkownicy/user.html')
        else:
                error = u'Form is invalid'
                return errorHandle(error,account_form)
    else:
        account_form = EditProfileForm(instance=account)
        return render_to_response("uzytkownicy/edit_profile.html", {
                                                                     'account_form':
                                                                     account_form,                                                                           
                                                                     })
                                     
        
            
        
        
            
            
    
    