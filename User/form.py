from .models import User
from django import forms


# If creating form using ModelForm
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('firstName','lastName','email', 'password', 'role')