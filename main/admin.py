from django.contrib import admin
from .models import Task
# Register your models here.

#admin panel will get this information
admin.site.register(Task)