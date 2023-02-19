from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFormulario, ProfesorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    #return HttpResponse('vista inicio')
""""
def cursos(request):
    return render(request, 'AppCoder/cursos.html')
    #return HttpResponse('vista cursos')
"""    
    

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], camada=informacion['apellido'], 
                                email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = ProfesorFormulario()
        
    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})        

#return render(request, 'AppCoder/profesores.html')
#return HttpResponse('vista profesores')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse('vista estudiantes')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')
    #return HttpResponse('vista entregables')
""""
def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada=19881)
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def cursoFormulario(request):
    if request.method == 'POST':
        curso = Curso(request.POST['curso'], (request.POST['camada']))
        curso.save()
        return render(request, "AppCoder/inicio.html")
    
    return render(request, "AppCoder/cursoFormulario.html")
"""

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = CursoFormulario()
        
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})        

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos, "camada":camada})
        #return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos" 

    #return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})
    
    
    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    
    return HttpResponse(respuesta)
    
    
def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)
    
def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    profesor = Profesor.objects.all()
    contexto= {"profesores":profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre =profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido'] 
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            
            profesor.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 
                                                   'apellido':profesor.apellido, 
                                                   'email':profesor.email, 
                                                   'profesion': profesor.profesion})
        
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})        

class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos_list.html"
    
class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"
    
class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']  
    
class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/list"