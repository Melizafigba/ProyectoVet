from django.shortcuts import render
from .models import Animal
from .forms import PostFormulario


# Create your views here.
def bienvenido(request):
    return render(request,'aplicacion/bienvenido.html',{})

def lista_post(request):
    animals = Animal.objects.all()
    return render(request,'aplicacion/lista_post.html',{'animals': animals})

def almacenar(request):
    animal = Animal()

    if request.method == 'POST':
        newAnimal = PostFormulario(request.POST, instance=animal)
        newAnimal.save()
        return render(request,'aplicacion/bienvenido.html',{})
    else:
        formulario = PostFormulario()
        return render(request,'aplicacion/almacenar.html',{'formulario':formulario})

def editar(request):
    animal = Animal()

    if request.method == 'POST':
        editAnimal = PostFormulario(request.POST, instance=animal)
        editAnimal.save()
        return render(request,'aplicacion/bienvenido.html',{})
    else:
        formulario = PostFormulario()
        return render(request,'aplicacion/editar.html',{'formulario':formulario})

    



    



