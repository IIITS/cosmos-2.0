from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from feasta.config import model_choices
from feasta import methods
from feasta.models import GuestAdd, SummerRegistration
class LoginForm(AuthenticationForm):
	username = forms.CharField(
		widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'id':'username',
			'placeholder':'Enter your username or email'
			}
		))
	password = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
			'class':'form-control',
			'id':'password',
			'placeholder':'Enter your password'
			}
		))

class SetPasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput(
                                    	attrs={'class':'form-control'}
                                    	))
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput(
                                    	attrs={'class':'form-control'}
                                    	))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class PasswordChangeForm(SetPasswordForm):
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': ("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=("Old password"),
                                   widget=forms.PasswordInput(
                                    	attrs={'class':'form-control'}
                                    	))

    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password
class SummerRegisterForm(forms.ModelForm):
	class Meta:
	        model = SummerRegistration
        	exclude = ('booked_by','booked_time')
class AddGuestForm(forms.ModelForm):
	class Meta:
        	model = GuestAdd
        	exclude = ('booked_by','booked_time')


