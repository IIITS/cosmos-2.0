from btp.models  import *
from btp.forms   import *
from btp.methods import *

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

class IndexView(TemplateView):
	template_name = 'index/index.html'
	def get_context_data(self, **kwargs):
		context=super(IndexView,self).get_context_data(**kwargs)
		context = {'title':'Cosmos'}
		
		return context
	def dispatch(self, *args, **kwargs):
		return super(IndexView,self).dispatch(*args,**kwargs)
class BTPIndexView(TemplateView):
	template_name = 'btp/btpindex.html'
			
	def get_context_data(self, **kwargs):
		context=super(BTPIndexView,self).get_context_data(**kwargs)
		
		students = Student.objects.order_by('user__username')
		faculty = Faculty.objects.order_by('user__first_name')
		batches = Batch.objects.order_by('graduate_year')
		
		context = {'title':'Home - BTP',
			   'students':students,
			   'faculty':faculty,
			   'header':'B-Tech Projects Portal',
                           'MEDIA_URL':settings.MEDIA_URL,
                'batches':batches           
			   		
		}
		context['is_fac'] = False
		if self.request.user.groups.filter(name='Faculty').count():
			context['is_fac'] = True
		return context
	def dispatch(self, *args, **kwargs):
		return super(BTPIndexView,self).dispatch(*args,**kwargs)

class LoginView(FormView):
	template_name = 'accounts/login.html'
	form_class = LoginForm
	success_url = settings.LOGIN_REDIRECT_URL
	def form_valid(self,form):
		username = form.cleaned_data['username']
	    	password = form.cleaned_data['password']
    		user = authenticate(username=username, password=password)
		
    		if user is not None:
			
        		if user.is_active:
				
            			login(self.request, user)
			return HttpResponseRedirect('/')
		return super(LoginView,self).form_valid(form)
	def form_invalid(self,form):
		return render(self.request, self.template_name, {'form': form, 'form_error':'Sorry, username or password incorrect!' } )
	def get_context_data(self,**kwargs):	
		context = super(LoginView,self).get_context_data(**kwargs)
		context = {'title':'Login - Septem',
			   'form':LoginForm(self.request.POST)	
		}
		return context

class AddProject(TemplateView):
	template_name = 'btp/add_project.html'


	def get_context_data(self,**kwargs):	
		context = super(AddProject,self).get_context_data(**kwargs)
		context = {'title':'Add project'		}
		return context

class EditProject(TemplateView):
	template_name = 'btp/edit_project.html'
	
	def get_context_data(self,**kwargs):	
		context = super(EditProject,self).get_context_data(**kwargs)
		projects = Project.objects.filter(supervisors__contains=str(self.request.user))
		context = {'title':'Manage Project', 'projects':projects, 'fileform':FileUploadForm }
		pa = ProjectArchives.objects.filter(supervisors__contains=self.request.user.username, restored=False)
		if pa.count() > 0:
			context['projects_are_archived']=True
			context['archived_projects']=pa
		else:
			context['projects_are_archived']=False
			context['archived_projects']=[]	
		return context		

class EditProjectInstance(TemplateView):
	template_name = 'btp/edit_project_instance.html'
	
	def get_context_data(self,**kwargs):	
		context = super(EditProjectInstance,self).get_context_data(**kwargs)
		pid = kwargs.get('id')
		project = Project.objects.get(id=pid)
		pro = {'title':project.title, 'description':project.description, 'btp':True, 'honors':False, 'si_yes':True, 
		'si_no':False, 'si_nyd':False, 'keywords':project.keywords, 'pid':project.id}

		if project.typeOfProject != 'btp':
			pro['honors'] = True
			pro['btp'] = False
		if project.summer == 'no':
			pro['si_yes'] = False
			pro['si_no'] = True
			pro['si_nyd'] = False
		if project.summer == 'nyd':
			pro['si_yes'] = False
			pro['si_no'] = False
			pro['si_nyd'] = True	
		context = {'title':'Manage Project', 'p':pro}
		return context	

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
@csrf_exempt
def submit_report( request):
	if request.is_ajax:
		usertype = getUserTypes(request.user)
		if "STUDENT" in usertype:
	           	form = SubmissionForm(request.FILES, request.POST)
		   	print request.FILES['fileuploaded']
		   	
                	fileuploaded = request.FILES['fileuploaded']
			
			pg = getProjectGroupByStudentId(getStudentIdByUser(request.user))
			evalset = getBTPEvalSetByProjectGroup(pg)
			getAllBTPProjectGroupsByEvalSet(evalset)		
			pgid = pg.id
                        response_data = {}
			print "here"
			try:
				currweek = getCurrentWeek()
				week = BTPSetWeek.objects.get(week = currweek, sets=evalset)
				try:
					submit = BTPSubmission.objects.get(week = week , projectgroup = pg)
					submit.fileuploaded = fileuploaded
					submit.submitted_by = request.user
					send_mail(subject, message, 'btpc@iiits.in',to_list, fail_silently=False)
		
					
					submit.save()
				except ObjectDoesNotExist as error:
					
					submit = BTPSubmission( week = week , projectgroup = pg, fileuploaded = fileuploaded, submitted_by = request.user )
					subject = getSubjectMail(submit)
					message = getContentMail(submit)
					to_list = getMailingList(submit)
					
					send_mail(subject, message, 'btpc@iiits.in',to_list, fail_silently=False)
					submit.save()
					response_data['status'] = 200	
				
			except ObjectDoesNotExist as error:
				week = BTPSetWeek.objects.all()[0]
				response_data['status'] = 500
				print "Here"
		return HttpResponseRedirect('/btp')
@csrf_exempt
def SubmitProject(request):
	f = Faculty.objects.get(user=request.user)
	f.get_all_projects()
	code = f.get_next_code()
	p = Project(code=code,title=request.POST.get('title'),
			description=request.POST.get('description'),
			summer=request.POST.get('summer'),
			keywords = request.POST.get('keywords'),
			typeOfProject=request.POST.get('typeOfProject'),
			students='', supervisors = str(request.user.username), year='2016'
		)
	p.save()
	return HttpResponseRedirect('/')


@csrf_exempt
def editSubmitProject(request):
	pro = Project.objects.get(id = request.POST.get('pid'))
	pro.title = request.POST.get('title')
	pro.description = request.POST.get('description')
	pro.keywords = request.POST.get('keywords')
	pro.typeOfProject = request.POST.get('typeOfProject')
	pro.summer = request.POST.get('summer')
	pro.save()
	return HttpResponseRedirect('/')

@csrf_exempt
def addStudentsToProject(request):
	pro = Project.objects.get(id = request.POST.get('pid'))
	pro.students = request.POST.get('students')
	pro.save()
	return HttpResponseRedirect('/')	

def getCurrentStudents(request):
	st = Student.objects.filter(year='2016')
	st_list = list()
	for s in st:
		st_list.append(
			{'user':s.user.username, 'name':s.user.get_full_name()})
	return JsonResponse(json.dumps({'students':st_list}), safe=False)	

@csrf_exempt
def uploadProjectFileFaculty(request, **kwargs):
	
	P = ProjectMedia(file_name=request.POST['file_name'],file_up=request.FILES['file_upload'], project = Project.objects.get(id=kwargs['id']))
	P.save()
	return HttpResponseRedirect('/edit-project/')


def deleteUploadedProjectMedia(request, **kwargs):
	ProjectMedia.objects.get(id=kwargs['id']).delete()
	return HttpResponseRedirect('/edit-project/')

def moveProjectToArchives(request, **kwargs):
	p = Project.objects.get(id=kwargs['id'])
	pa = ProjectArchives(code = p.code,
						title =  p.title,
						description = p.description,
						keywords = p.keywords,
						typeOfProject= p.typeOfProject,
						supervisors = p.supervisors,
						year= p.year,
						summer =p.summer)
	pa.save()
	p.delete()
	return HttpResponseRedirect('/edit-project/')						

def restoreFromArchives(request, **kwargs):
	pid = kwargs['id']
	pa = ProjectArchives.objects.get(id=pid)
	p = Project(code=pa.code,
			title=pa.title,
			description=pa.description,
			keywords=pa.keywords,
			typeOfProject=pa.typeOfProject,
			supervisors=pa.supervisors,
			summer=pa.summer,
			year=pa.year)
	p.save()
	pa.restored = True
	return HttpResponseRedirect('/edit-project/')