from django.shortcuts import render

# Create your views here.
def registro(req):
    return render(req, "registro.html")

def inicio(req):
    return render(req, "inicio.html")

def login(req):
    return render(req, "login.html")

def reg_usuario(req):
    return render(req, "registro_usuario.html")