from __future__ import unicode_literals
from django.db import models

# Create your models here.
class PasswordResetOTPLogs(models.Model):
	otp = models.CharField(max_length=10)
	user_email = models.CharField(max_length=150)
	expired = models.BooleanField(default=False)
	reset_request_time = models.DateTimeField(auto_now_add=True)
	last_access_time = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.otp
