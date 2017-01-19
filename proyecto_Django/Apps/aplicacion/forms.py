from django import forms
from Apps.aplicacion.models import Persona

class Formularioregistro(forms.ModelForm):
		class Meta:
			model = Persona

			fields = [
			'tipo_documento',
			'id_documento',
			'nombre',
			'apellido',
			'edad',
			'telefono',
			'email',
			]	
			labels = {
			'tipo_documento':'Tipo de documento',
			'id_documento':'Numero de documento',
			'nombre':'Nombre',
			'apellido':'Apellido',
			'edad':'edad',
			'telefono':'Telefono',
			'email':'Email',
			}
			widgets = {
			'tipo_documento': forms.TextInput(attrs={'class':'form-control'}),
			'id_documento': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			}
			