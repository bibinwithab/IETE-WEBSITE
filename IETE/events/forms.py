from django import forms
from .models import Registration

# creating a form
class RegisterForm(forms.Form):

	name = forms.CharField(max_length = 200)
	email = forms.EmailField()
	phone = forms.IntegerField(max_value=10)
	college = forms.CharField(max_length=100)
	branch = forms.CharField(max_length=100)
	year = forms.CharField(max_length=100)

	class Meta:
		model = Registration
		fields="__all__"
