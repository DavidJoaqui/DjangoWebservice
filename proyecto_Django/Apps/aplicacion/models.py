from django.db import models

# Create your models here.
class Persona(models.Model):

	id_documento=models.CharField(max_length=15, primary_key=True)
	tipo_documento=models.CharField(max_length=50)
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	edad=models.IntegerField()
	telefono=models.CharField(max_length=12)
	email=models.EmailField()
	
