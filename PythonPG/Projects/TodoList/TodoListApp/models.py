from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=200)

class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)