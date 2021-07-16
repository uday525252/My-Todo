from django.contrib import admin
from todoapp.models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ['task']


admin.site.register(Todo, TodoAdmin)
