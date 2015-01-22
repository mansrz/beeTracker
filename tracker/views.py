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
    #mejorar el query, se tiene el id_device
    user=request.user
    device = Supervisor.objects.get(user = user.id).devices.get(id =id_device)
    user_data = device.positions.last()
    data_location = []
    data_location.append(user_data.latitude)
    data_location.append(user_data.longitude)
    data_location.append(user_data.speed)
    data_location.append(device.name)

    return HttpResponse(json.dumps(data_location))

@login_required(login_url='/login')
def checkPoints(request, id_device):
    checkpoints = Device.objects.get(id = id_device).checkPoint.all()
    checkpoints_data = []
    for checkpoint in checkpoints:
        cp = []
        cp.append(checkpoint.latitude)
        cp.append(checkpoint.longitude)
        cp.append(checkpoint.campo1)
        cp.append(checkpoint.campo2)
        cp.append(checkpoint.campo3)
        cp.append(str(checkpoint.picture))
        checkpoints_data.append(cp)

    return HttpResponse(json.dumps(checkpoints_data))

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
        return render_to_response('movilPost/new_device.html',  RequestContext(request))

@login_required(login_url='/')
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
                    device = Device.objects.get(id = id_device)
                    device.positions.add(position)
                    return HttpResponse(json.dumps(1))
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
        return render_to_response('movilPost/new_position.html',  RequestContext(request))


@login_required(login_url='/logout')
def newCheckPoint(request):
    if request.method == 'POST':
        try:
            id_device = request.POST['id_device']
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
            campo1 = request.POST['value_1']
            campo2 = request.POST['value_2']
            campo3 = request.POST['value_3']
            picture = request.FILES['picture']
            user=request.user
            if user is not None:
                if user.is_active:
                    # The user is Authentic
                    device = Device.objects.get(id = id_device)
                    checkpoint = CheckPoint(latitude=latitude,longitude=longitude, campo1=campo1,campo2=campo2,campo3=campo3,picture=picture)
                    checkpoint.save()
                    device.checkPoint.add(checkpoint)
                    device.save()
                    return HttpResponse(json.dumps(1))
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
        return render_to_response('movilPost/new_check_point.html',  RequestContext(request))

'''
TRANSESPOL START
'''
def transespol(request):
    import requests, re
    response = requests.session().post("http://fs.teccial.com:8081/WSEspol/interfaces/interfaceSeguridad.php", {"txt_user": "transespol", "txt_pass": "espol2"}).text
    patronBus = re.compile('<(.+?)>')
    patronInfo = re.compile('\((.+?)\)')
    try:
        buses = patronBus.findall(response)
        buses[0]=buses[1]
        for bus in buses:
            de = Device.objects.get(name = patronInfo.findall(bus)[1])
            de.positions.create(latitude = float(patronInfo.findall(bus)[3]), longitude= float(patronInfo.findall(bus)[2]))
            de.save()
    except:
        pass
    return HttpResponse(json.dumps(True))
'''
TRANSESPOL END
'''

#cambiar las variables de con las que se recibe del HTML