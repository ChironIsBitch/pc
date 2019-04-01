# from django.contrib import admin
import xadmin
from .models import Start
# Register your models here.


class StartAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ('id', 'name', 'start_time')
    ordering = {'id'}


xadmin.site.register(Start, StartAdmin)

