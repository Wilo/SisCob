#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
import django
import json
from django.http import HttpRequest
#from siscobros.apps.main.forms import * return render_to_response('main/login.html', context_instance=RequestContext(request))
# Create your views here.
#Ventana de Inicio de sesion

def index_view(request):
    login = LoginForm
    return render(request, 'main/login.html',locals())

def enviar_ajax(request):
    usuario = request.POST['usuario']
    password = request.POST['password']
    data = {'usuario':usuario,'password':password}
    return HttpResponse(json.dumps(data),mimetype='application/json')


@login_required(login_url="/")
def main_view(request):
    usuario = request.user
    return render_to_response('main/index.html',{'usuario':usuario} ,content_type=RequestContext(request))

# @login_required(login_url="/")
def error_view(request):
    return render_to_response('main/autocomplete.html',content_type=RequestContext(request))

def Demo_view(request):
    if request.method=='POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/main/index.html')
    else:
        form = DemoForm()
        return render_to_response('main/demo.html', {'form': form }, content_type=RequestContext(request))

def autocomplete(request):
    return render_to_response('main/autocomplete.html',content_type=RequestContext(request))

def get_value(request):
    if request.method == "POST":
        txt1 = request.POST['txtIngreso1']
        txt2 = request.POST['txtIngreso2']
        suma = txt1+txt2
        print suma
        return HttpResponse({'suma':suma},content_type=RequestContext(request))

# def get_Ciudadela(request):
#     if request.is_ajax():
#         q = request.Get.get('term','')
#         ciudadelas = Ciudadela.objects.filter(Descripcion__icontains=q)
#         results = []
#         for ciudadela in ciudadelas:
#             ciudadela_json ={}
#             ciudadela_json['Desc'] = ciudadela.Descripcion
#             results.append(ciudadela_json)
#         data = json.dump(results)
#     else:
#         data = 'Error'
#     mimetype = 'application/json'
#     return HttpResponse(data,mimetype)





# Features por Probar luego
# def login_view(request):
#     mensaje = ""
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/')
#     else:
#         if request.method == "POST":
#             form = LoginForm(request.POST)
#             if form.is_valid():
#                 next = request.POST['next']
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 usuario = authenticate(username=username,password=password)
#                 if usuario is not None and usuario.is_active:
#                     login(request,usuario)
#                     return HttpResponseRedirect(next)
#                 else:
#                     mensaje = "usuario y/o password incorrecto"
#         next = request.REQUEST.get('next')
#         form = LoginForm()
#         ctx = {'form':form,'mensaje':mensaje,'next':next}
#         return render_to_response('main/login.html',ctx,context_instance=RequestContext(request))


    # mensaje = ""
    # if request.user.is_authenticated():
    #     HttpResponseRedirect('/')
    # else:
    #     if request.method == "POST":
    #         form = LoginForm(request.POST)
    #         if form.is_valid():
    #             username = form.cleaned_data['username']
    #             password = form.cleaned_data['password']
    #             usuario = authenticate(username=username, password=password)
    #             if usuario is not None and usuario.is_active:
    #                 login(request, usuario)
    #                 return HttpResponseRedirect('/')
    #             else:
    #                 mensaje="Usuario o Contraseña incorrectos"
    #
    #     form = LoginForm()
    #     ctx = {'form':form, 'mensaje': mensaje}
    #     return render_to_response('main/login.html', ctx, _context_instance=RequestContext)


# def logout(request):
#     logout(request)
#     return HttpResponseRedirect('/')

#comentario
# var = Ciudadela.objects.all().order_by("-Fecha") con esto hago select a las ultimas transacciones