from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm, LoginForm, ReclamoForm, UsuariosForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login 
# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')

def contacto(request):
    return render(request,'aplicacion/contacto.html')

def recibir(request):
    return render(request,'aplicacion/recibir.html')    

def clientes(request):
    cliente=Cliente.objects.all()
    return render(request, 'aplicacion/clientes.html',{'data':cliente})

def reclamo2(request):
    if request.method=='POST':
        form = ReclamoForm(data = request.POST)
        email = form['email']
        reclamo = form['reclamo']
        return render(request,'aplicacion/reclamoejemplo.html',{'respuesta':'OK'})
    else:
        form = ReclamoForm()
        return render(request,'aplicacion/reclamoejemplo.html',{"form":form})

def crearUsuario(request):
    if request.method=='POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            clave = form.cleaned_data['password']
            grupo = form.cleaned_data['grupo']
            user = User.objects.create_user(nombre,email,clave)
            user.save()
            group = Group.objects.get(name=grupo)
            user.groups.add(group)
            user.save()
        return render(request,'aplicacion/usuariocreado.html')
    else:
        form = UsuariosForm()
        return render(request, 'aplicacion/crearusuario.html',{'form':form})
def clientes2(request):
    if request.method=='POST':
        form=ClienteForm(data = request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)#esta en memoria
            cliente.save()#guarda en base de datos
        return redirect('/clientes')
    else:
        form=ClienteForm()
        return render(request,'aplicacion/crearcliente.html',{'form':form})

def loginu(request):
    if request.method=='POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clave = form.cleaned_data['password']
            user = authenticate(request, username = nombre, password = clave)
            if user is not None:
                login(request,user)
        return render(request,'aplicacion/bienvenido.html',{'user':user})
    else:
        form = LoginForm()
        return render(request,'aplicacion/loginu.html',{'form':form})

def grupito(request):
    user = User.objects.create_user('valeria','v@empresa.cl','qweqweqweqwe')
    user.save()
    group = Group.objects.get(name='grupo1')
    user.groups.add(group)
    user.save()
    return render(request,'aplicacion/usuariocreado.html')