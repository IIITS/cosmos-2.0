from django.views.generic.edit import FormView
from django.http import HttpResponse
from btp.forms import CommandForm
from os import system as shell_execute
import json

class GitCommand(FormView):
	form_class = CommandForm
	template_name = 'btp/git.html'
	def get_context_data(self,**kwargs):
		return super(GitCommand, self).get_context_data(**kwargs)
	def form_valid(self, form):
		command = form.cleaned_data['command']
		shell_execute("%s > results.txt" %(command))
		f = open("results.txt", "r")
		p = f.readlines()
		k =""
		for x in p:
			k+= x.strip()+"<br>"
		
		f.close()
		return HttpResponse(k)
