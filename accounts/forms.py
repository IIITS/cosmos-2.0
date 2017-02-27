from django.forms import *

class EmailPostForm(Form):
	email = CharField(widget=TextInput(attrs={'class':'mdl-textfield__input', 'id':'user_email'}))

class OTPForm(Form):
	otp = CharField(widget=TextInput(attrs={'class':'mdl-textfield__input', 'id':'otp'}))