# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    latitude =  models.FloatField(max_length=17)
    longitude =  models.FloatField(max_length=17)
    altitude =  models.TextField(max_length=12, blank= True, null= True)
    speed =  models.TextField(max_length=5, blank= True, null= True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return str(self.latitude)

    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"

class CheckPoint(models.Model):
    latitude =  models.FloatField(max_length=17, default= 0.0)
    longitude =  models.FloatField(max_length=17, default= 0.0)
    campo1 =  models.TextField(max_length=25, blank= True, null= True)
    campo2 =  models.TextField(max_length=25, blank= True, null= True)
    campo3 =  models.TextField(max_length=25, blank= True, null= True)
    picture = models.ImageField(upload_to='checkPoint/%Y/%m/%d',verbose_name='Picture', null= True,  default='checkPoint/anonymous.png')

    def __unicode__(self):
        return self.campo1

    class Meta:
        verbose_name = "CheckPoint"
        verbose_name_plural = "CheckPoints"

class Device(models.Model):
    positions = models.ManyToManyField(Position, related_name='Positions', blank= True, null= True)
    checkPoint = models.ManyToManyField(CheckPoint, related_name='CheckPoints', blank= True, null= True)
    name = models.TextField(max_length=20, blank= True, null= True)
    #supervisor = models.ForeignKey(Supervisor, related_name='Supervisor')
    status = models.BooleanField(default=True)
    description = models.TextField(max_length=50, blank= True, null= True)
    #Borrar modelo y version descomentar status y descripcion >> modificar newDeviceForm
    #model = models.TextField(max_length=12, blank= True, null= True)
    version = models.TextField(max_length=12, blank= True, null= True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    picture = models.ImageField(upload_to='devices/%Y/%m/%d',verbose_name='Devices', null= True,  default='devices/anonymous.png')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

class Supervisor(models.Model):
    #user = models.OneToOneField(User)
    user = models.ForeignKey(User)
    devices = models.ManyToManyField(Device, related_name='Devices')
    picture = models.ImageField(upload_to='users/%Y/%m/%d',verbose_name='Users', null= True,  default='users/anonymous.png')
    date = models.DateTimeField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisores"
