from django.shortcuts import render

# Create your views here.
from btp.models  import *
from btp.forms   import *
from btp.methods import *
from accounts.forms import *
from accounts.models import *
from accounts.methods import *
from django.core.exceptions import *
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url,render
from django.template.response import TemplateResponse
from django.core.mail import send_mail
import json
from django.contrib.auth.models import User
import ldap
from django_auth_ldap import backend 

  

class LoginView(FormView):
	template_name = 'accounts/login.html'
	form_class = LoginForm
	success_url = settings.LOGIN_REDIRECT_URL
	def form_valid(self,form):
		username = form.cleaned_data['username']
	    	password = form.cleaned_data['password']
    		user = authenticate(username=username, password=password)
	        ldap_backend = backend.LDAPBackend()
        	ldap_user = backend.LDAPBackend.authenticate(ldap_backend, username=username, password=password)

    		if user is not None:
			
        		if user.is_active:
				
            			login(self.request, user)
			return HttpResponseRedirect('/')
		if ldap_user is not None: 
			login(self.request, user)
			return HttpResponseRedirect('/')
        	print "here"    
		return super(LoginView,self).form_valid(form)
	def form_invalid(self,form):
		return render(self.request, self.template_name, {'form': form, 'form_error':'Sorry, username or password incorrect!' } )
	def get_context_data(self,**kwargs):	
		context = super(LoginView,self).get_context_data(**kwargs)
		context = {'title':'Login - Septem',
			   'form':LoginForm(self.request.POST)	
		}
		return context

class NewPasswordView(FormView):
    
    template_name = 'accounts/login.html'
    form_class = NewPasswordForm
    success_url = settings.LOGIN_REDIRECT_URL
    
    def form_valid(self,form):
        
        pass1 = form.cleaned_data['password']
        pass2 = form.cleaned_data['password_again']
        
        if pass1 == pass2:
            form.save()
            return HttpResponseRedirect('/')
        return super(NewPasswordView,self).form_valid(form)

    def form_invalid(self,form):
        
        return render(self.request, self.template_name, {'form': form, 'form_error':'Sorry, There was an error. Choose a password of length 8 or more' } )
    
    def get_context_data(self,**kwargs):    
        
        context = super(NewPasswordView,self).get_context_data(**kwargs)
        context = {'title':'Login - Septem',
               'form':NewPasswordForm(self.request.POST)  
        }
        return context

    def dispatch(self, *args, **kwargs):
        
        email = self.kwargs['user_email']
        otp = self.kwargs['otp']

        try:
            pr_otp = PasswordResetOTPLogs.objects.get(otp=otp, user_email=email, expired=False)
            return super(NewPasswordView,self).dispatch(*args,**kwargs)

        except ObjectDoesNotExist:
            return HttpResponseRedirect('/accounts/send-otp/lost-password/')    


@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='accounts/password_change_form.html',
                    post_change_redirect = None,
                    password_change_form=ChangePasswordForm,
                    extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('password_change_done')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': ('Password change'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)
	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

class UnderConstruction(TemplateView):
	
    template_name = 'index/underconstruction.html'

    def dispatch(self, *args, **kwargs):
		return super(UnderConstruction,self).dispatch(*args, **kwargs)

class SendOtpView(FormView):

    template_name = 'accounts/send_otp.html'
    form_class=EmailPostForm
    def get_context_data(self, **kwargs):
        return {'form':EmailPostForm()}

    def form_invalid(self,form):
        return render(self.request, self.template_name, {'form': form, 'form_error':'Looks like you are not on cosmos!' } )
    
    def form_valid(self, form):
            otp = createOTP()
            email = form.cleaned_data['email']
            try:
                p = PasswordResetOTPLogs(otp = otp ,user_email=email)
                p.save()
                user = User.objects.get(email=email)
                name = user.get_full_name()
                subject = "[Cosmos@IIITS] Password Reset - One Time Password"
                to = [user.email]
                bcc = ["sahalsajjad@gmail.com"]
                from_email = '[do-not-reply] Cosmos support <no-reply@cosmos.iiits.in>'
                ctx = {
                    'title':'[Cosmos] Password Reset - OTP',
                    'otp':otp,
                    "name":name
                }

                message = get_template('email/otp_email.html').render(Context(ctx))
                msg = EmailMessage(subject, message, to=to, from_email=from_email, bcc=bcc)
                msg.content_subtype = 'html'
                msg.send()
                return HttpResponseRedirect('/accounts/verify-otp/lost-password/?user_email=%s' %(user.email))   

            except ObjectDoesNotExist:   
                return render(self.request, self.template_name, {'form': form, 'form_error':'The email you entered is not associated with any account on cosmos!'})

class VerifyOtpView(FormView):

    template_name = 'accounts/verify_otp.html'   
    form_class = OTPForm
    success_url = '/accounts/new-password/'
    
    def get_context_data(self,**kwargs):
        return {'email':self.kwargs['user_email'], 'form':OTPForm()}     
    
    def form_valid(self, form):
            try:
                email = self.kwargs['user_email']
                otp = form.cleaned_data['otp']
                pr_otp = PasswordResetOTPLogs.objects.get(otp=otp,user_email=email)
                return HttpResponseRedirect('/acounts/new-password/?user_email=%s&otp=%s'%(email,otp))    

            except ObjectDoesNotExist:   
                return render(self.request, self.template_name, {'form': form, 'form_error':'OTP entered is incorrect. Please check your email and try again' })
            
    def form_invalid(self,form):
        return render(self.request, self.template_name, {'form': form, 'form_error':'OTP entered is incorrect. Please check your email' } )
    
          
