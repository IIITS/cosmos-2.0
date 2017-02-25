from django.forms import *

class EmailPostForm(Form):
	email = CharField(widget=TextInput(attrs={'class':'mdl-textfield__input', 'id':'user_email'}))

class OTPForm(Form):
	otp = CharField(widget=TextInput(attrs={'class':'mdl-textfield__input', 'id':'otp'}))
class NewPasswordForm(Form):
	new_password1=CharField(widget=TextInput(attrs={'class':'mdl-textfield__input', 'id':'password'}))
	new_password2=CharField(widget=TextInput(attrs={'class':'mdl-textfield__input', 'id':'password_again'}))