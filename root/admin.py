from django.contrib import admin
from .models import Service


class Adminservice(admin.ModelAdmin):
    list_display = ['title', 'contact','status']
    list_filter = ['status']
    search_fields = ['title']
admin.site.register(Service,Adminservice)
# Register your models here.
