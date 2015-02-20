from django.contrib import admin
from tracker.models import *

class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date',)
    search_fields = ('user__username',)
    list_filter = ('date',)
    ordering = ('-date',)

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'date', 'pk', 'picture','status',)
	search_fields = ('name',)
	list_filter = ('date',)
	ordering = ('-date',)

class CPAdmin(admin.ModelAdmin):
	list_display = ('id', 'campo1', 'campo2', 'date','picture','pk')
	search_fields = ('name','campo1')
	list_filter = ('date',)
	ordering = ('-date',)	

admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Position)
admin.site.register(Device, DeviceAdmin)
admin.site.register(CheckPoint, CPAdmin)
