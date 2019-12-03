

from .models import User
from django import forms


# If creating form using ModelForm
class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)
	role = forms.ChoiceField(choices=(("user",("user")),("admin",("admin"))))
	class Meta:
		model = User
		fields = ('firstName','lastName','email', 'username', 'password', 'role')