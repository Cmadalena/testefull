from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from lapp.forms import FuncionarioForm



# Create your views here.
def home(request):
    return render(request, 'login.html')


# formulario de cadastro de utilizadores.
def create(request):
    return render(request, 'create.html')


# insercao dos dados na bd
def store(request):
    data = {}
    #verificando se as passwords sao iguais.
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e a confirmacao da senha sao diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(25)
        data['msg'] = 'Utilizador Cadastrado com Sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)


def fhome(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = FuncionarioForm.objects.filter(modelo__icontains=search)
    else:
        data['db'] = FuncionarioForm.objects.all()
    return render(request, 'home.html', data)


# form create employer
def form(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'cadastrofuncionario.html', data)


# insert employer
def createfuncionario(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


# formulario de painel de login
def painel(request):
    return render(request, 'painel.html')


def flogin(request):
    return render(request, 'login.html')


# process login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Utilizador ou Senha Invalida!'
        data['class'] = 'alert-danger'
        return render(request, 'login.html', data)


# Pagina Inicial do Dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')


# logouts
def logouts(request):
    logout(request)
    return redirect('/login/')


# Alterar a Senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/painel/')