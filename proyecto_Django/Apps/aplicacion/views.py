from django.shortcuts import render_to_response, redirect, render

from .forms import Formularioregistro
from .models import Persona
# Create your views here.



def formulario(request):
	if request.method == 'POST':
		form=Formularioregistro(request.POST or None)
		if form.is_valid():
			form.save()
		return redirect('Home')	
	else:
		form=Formularioregistro()
	return render(request,'Home.html',{'form':form})	

def documentacion(request):
	return render(request,'documentacion.html');

def contacto(request):
	return  render(request,'contacto.html')

def listar(request):
	persona = Persona.objects.all()
	contexto={'personas':persona}
	return render(request,'listaPersonas.html',contexto)

def editarpersona(request, id_documento):
	persona=Persona.objects.get(id_documento=id_documento)
	if request.method=='GET':
		form=Formularioregistro(instance=persona)
	else:
		form = Formularioregistro(request.POST,instance=persona)
		if form.is_valid():
			form.save()
		return redirect('listar')	
	return render(request,'Home.html',{'form': form})

def eliminarRegistro(request, id_documento):
	persona=Persona.objects.get(id_documento=id_documento)
	if request.method == 'POST':
		persona.delete()
		return redirect('listar')
	return render(request,'eliminarRegistros.html',{'personadelete':persona})	
