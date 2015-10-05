from django import forms
from sif.apps.inventario.models import *
from sif.apps.home.models import *
from django.contrib.auth.models import User

rol = (
	(u'admin', u'Administrador'),
	(u'oper', u'Operador'),
	)

#user
class RegisterForm(forms.Form):
	email			= forms.CharField(label = "Correo Electronico", widget = forms.TextInput())
	tipo 			= forms.ChoiceField(label = "Tipo Usuario", choices = rol)
	password_one	= forms.CharField(label = "Password", widget = forms.PasswordInput(render_value = False))
	password_two 	= forms.CharField(label ="Confirmar Password", widget = forms.PasswordInput(render_value = False))
	

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email = email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')

	def clean_password_two (self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')

#usuario
class add_usuario_form(forms.ModelForm):
	class Meta:
		model  = Usuario
		exclude= {'user'}


#Login

class Login_form(forms.Form):
	usuario 	= forms.CharField(widget = forms.TextInput())
	clave 		= forms.CharField(widget = forms.PasswordInput(render_value = False))


