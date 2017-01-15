from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from feasta.models import *
from feasta.config import *
from feasta.forms import *
from feasta import methods
from django.utils.timezone import now, datetime as Date
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
NUM_PAG_MAX = 5


# Create your views here.
def not_found(request):
	return render(request, '404.html', status=404)

def home(request):
	return render(request, 'mess_home.html')

class Home(TemplateView):
	template_name = 'mess_home.html'
	def get_context_data(self,**kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		if not self.request.user.is_active:
			return HttpResponseRedirect(settings.LOGIN_URL)
		return super(Home,self).dispatch(*args,**kwargs)
class Login(FormView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = settings.LOGIN_REDIRECT_URL
		
	def form_valid(self,form):
		redirect_to = settings.LOGIN_REDIRECT_URL
        	login(self.request, form.get_user())
        	if self.request.session.test_cookie_worked():
           		self.request.session.delete_test_cookie()
        	return HttpResponseRedirect(redirect_to) 
	
	def form_invalid(self,form):	
		return super(Login, self).form_invalid(form)
	@method_decorator(sensitive_post_parameters())	
	def dispatch(self, *args, **kwargs):
		if self.request.user.is_active:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
		return super(Login,self).dispatch(*args, **kwargs)
	def get_context_data(self, **kwargs):
			context = super(Login,self).get_context_data(**kwargs)
			context['form']=self.form_class
			return context


class MarkAbsentView(TemplateView):
	template_name = 'mark_absent.html'
	success_url=settings.LOGIN_REDIRECT_URL
	def get_context_data(self, **kwargs):
		context=super(MarkAbsentView,self).get_context_data(**kwargs)
		context['session_end_days']=methods.getSessionEndDays()
		context['user']=self.request.user
		return context
	
				
class MenuView(TemplateView):
	template_name = 'menu.html'
	def get_context_data(self, **kwargs):
		context=super(MenuView,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context


class MyAccount(TemplateView):	
	template_name = 'myaccount.html'
	def get_context_data(self, **kwargs):
		context=super(MyAccount,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
class EditProfile(FormView):
	template_name = 'editprofile.html'
	def get_context_data(self, **kwargs):
		context = super(EditProfile,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
class MyProfile(TemplateView):
	template_name = 'myprofile.html'
	def get_context_data(self, **kwargs):
		context = super(MyProfile,self).get_context_data(**kwargs)
		user = self.request.user
		context = {}
		context['user']=user
		user_type = methods.getUserType(user)
		context['user_type'] = user_type
		result=[]
		if user_type == "STUDENT" :
			try:
				not_eaten = methods.getNotEaten(user)
				context['NUM_BF_NOT_EATEN'] = len(not_eaten['bf'])
				context['NUM_LUNCH_NOT_EATEN'] = len(not_eaten['lunch'])
				context['NUM_DINNER_NOT_EATEN'] = len(not_eaten['dinner'])
				context['BF_NOT_EATEN'] = not_eaten['bf']
				context['LUNCH_NOT_EATEN'] = not_eaten['lunch']
				context['DINNER_NOT_EATEN'] = not_eaten['dinner']
				paginator = Paginator(not_eaten[3], NUM_PAG_MAX) 
		                page = self.request.GET.get('page')
    			
			except IndexError as Error:
				context['BF_NOT_EATEN'] = ["Not Available at the moment"]
				context['LUNCH_NOT_EATEN'] = ["Not Available at the moment"]
				context['DINNER_NOT_EATEN'] = ["Not Available at the moment"]
			try:
        			result = paginator.page(page)
    			except PageNotAnInteger:
        			result = paginator.page(1)
    			except EmptyPage:
        			result = paginator.page(paginator.num_pages)
        	context['TOTAL_UNREGISTERED'] = result		
		return context

class ListForMeal(TemplateView):
	template_name = 'listformeal.html'	
	def get_context_data(self, **kwargs):
		context=super(ListForMeal,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
class SummerRegisterView(FormView):
    form_class = SummerRegisterForm
    template_name = 'summer_register.html'
    success_url=settings.LOGIN_REDIRECT_URL
	
    def form_valid(self, form):
        reg = form.save(commit=false)
        reg.booked_by = self.request.user
        reg.save()
        return HttpResponseRedirect(success_url)
    def form_invalid(self, form):
    	return super(SummerRegisterView,self).form_invalid(form)    
    def get_context_data(self, *args, **kwargs):
    	context = super(SummerRegisterView, self).get_context_data(*args, **kwargs)
    	context={'form':SummerRegisterForm}
    	return context
class AddGuestView(FormView):
    form_class = AddGuestForm
    template_name = 'add_guest.html'
    success_url=settings.LOGIN_REDIRECT_URL
	
    def form_valid(self, form):
    	reg=form.save()
        reg = form.save(commit=false)
        reg.booked_by = self.request.user
        reg.save()
        return HttpResponseRedirect(success_url)
    def form_invalid(self, form):
    	return super(AddGuestView,self).form_invalid(form)    
    def get_context_data(self, *args, **kwargs):
    	context = super(AddGuestView, self).get_context_data(*args, **kwargs)
    	context={'form':AddGuestForm}
    	return context
    	
class PickDatesView(FormView):    	
    form_class = AddGuestForm
    template_name = 'add_guest.html'
    success_url=settings.LOGIN_REDIRECT_URL
	
    def form_valid(self, form):
    	reg=form.save()
        reg = form.save(commit=false)
        reg.booked_by = self.request.user
        reg.save()
        return HttpResponseRedirect(success_url)
    def form_invalid(self, form):
    	return super(PickDatesView,self).form_invalid(form)    
    def get_context_data(self, *args, **kwargs):
    	context = super(PickDatesView, self).get_context_data(*args, **kwargs)
    	context={'form':AddGuestForm}
    	return context
@csrf_exempt
def markAbsent(request):
	d = int(request.POST['d'])
	m = int(request.POST['m'])
	y = int("20"+str(request.POST['y']))
	date = Date(day=d,month=m,year=y,tzinfo=now().tzinfo)
	print date
	return HttpResponse('Marked Absent')
