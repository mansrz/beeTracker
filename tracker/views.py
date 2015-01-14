# -*- coding: utf-8 -*-
from tracker.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
import json

@login_required(login_url='/login')
def lastLocation(request, id_device):
    user=request.user
    user_data = Supervisor.objects.get(user = user.id).devices.get(id =id_device).positions.last()
    data_location = []
    data_location.append(user_data.latitude)
    data_location.append(user_data.longitude)
    data_location.append(user_data.speed)
    
    return HttpResponse(json.dumps(data_location))

@login_required(login_url='/login')
def devices(request):
    user=request.user
    user_data = Supervisor.objects.get(user = user.id)
    devices = user_data.devices.all()
    data_devices = []
    info_device = []
    for device in devices:
        data_devices.append(device.id)
        data_devices.append(device.name)
        data_devices.append(device.model)
        data_devices.append(device.version)
        data_devices.append(str(device.date))
        data_devices.append(str(device.picture))
        info_device.append(data_devices)
        data_devices = []
    return HttpResponse(json.dumps(info_device))

@login_required(login_url='/login')
def visor(request):
    user=request.user
    user_data = Supervisor.objects.get(user = user.id)
    devices = user_data.devices.all()

    return render_to_response('visor.html',{'devices':devices, 'user':user_data}, context_instance=RequestContext(request))

def login(request):
    if not request.user.is_anonymous():
    	# The user is Authenticate yet.
        return HttpResponseRedirect('/visor/')

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username=usuario,password=clave)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    # The user is Authentic
                    return HttpResponseRedirect('/visor/')
                else:
                	# The User is not Active
                	message = 'Tu cuenta ha sido suspendida, contacta al administrador por favor.'
                	return render_to_response('login.html',{'status':message}, context_instance= RequestContext(request))
            else:
            	# Is not User
            	message = 'Por favor revise que su usuario y contraseña sea la correcta.'
                return render_to_response('login.html',{'status':message}, context_instance= RequestContext(request))
    else:
        form = AuthenticationForm()
    # Render the AuthenticationForm empty
    return render_to_response('login.html',{'form':form}, context_instance=	RequestContext(request))

@login_required(login_url='/login')
def home(request):
    user=request.user
    user_data = Supervisor.objects.get(user = user.id)
    devices = user_data.devices.all()
    return render_to_response('home.html', {'devices':devices, 'user':user_data}, context_instance=RequestContext(request))


# POSTs from the devices
#@login_required(login_url='/logout')
def newDevice(request):
    if request.method == 'POST':
        try:
            usuario = request.POST['username']
            clave = request.POST['password']
            name = request.POST['name']
            user = authenticate(username=usuario,password=clave)
            response = []

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    # The user is Authentic
                    username = user.username
                    device = Device(name = name)
                    device.save()
                    supervisor = Supervisor.objects.get(user = user.id)
                    supervisor.devices.add(device)
                    id_device = device.id
                    response.append(username)
                    response.append(id_device)
                    response.append(name)
                    return HttpResponse(json.dumps(response))
                else:
                    # The User is not Active
                    message = 'Tu cuenta ha sido suspendida, contacta al administrador por favor.'
                    return HttpResponse(json.dumps(message))
            else:
                # Is not User
                message = 'Por favor revise que su usuario y contraseña sea la correcta.'
                return HttpResponse(json.dumps(message))
        except:
            return HttpResponseRedirect('/logout/')
    else:
        return HttpResponseRedirect('/logout/')
    return HttpResponseRedirect('/logout/')

@login_required(login_url='/logout')
def newPosition(request):    
    if request.method == 'POST':
        try:
            id_device = request.POST['id_device']
            lat = request.POST['latitude']
            lon = request.POST['longitude']
            speed = request.POST['speed']
            user=request.user
            if user is not None:
                if user.is_active:
                    # The user is Authentic
                    position = Position(latitude=lat,longitude=lon,speed=speed)
                    position.save()
                    supervisor = Supervisor.objects.get(user = user.id)
                    device = supervisor.devices.get(id = id_device)
                    device.positions.add(position)
                    return HttpResponse(json.dumps("1"))
                else:
                    # The User is not Active
                    message = 'Tu cuenta ha sido suspendida, contacta al administrador por favor.'
                    return HttpResponse(json.dumps(message))
            else:
                # Is not User
                message = 'Por favor revise que su usuario y contraseña sea la correcta.'
                return HttpResponse(json.dumps(message))
        except:
            return HttpResponseRedirect('/logout/')
    else:
        return HttpResponseRedirect('/logout/')
    return HttpResponseRedirect('/logout/')


@login_required(login_url='/logout')
def newCheckPoint(request):
    pass
