from django.contrib import admin
from .models import TodoItem, TodoList

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(TodoList)