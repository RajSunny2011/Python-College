from django.shortcuts import render, redirect
from .models import  TodoList, TodoItem

# Create your views here.
def indexview(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'index.html', {'todo_lists': todo_lists})

def add_todo_list_function(request):
    name = request.POST['name']
    todo_list = TodoList(name = name)
    todo_list.save()
    return redirect('indexname')

def add_todo_item(request):
    todo_list_item = request.POST['todo_list_id']
    text = request.POST['text']
    todo_item = TodoItem(todo_list_item = todo_list_item, text = text)
    todo_item.save()
    return redirect('indexname')

def delete_todo_list(request):
    todo_list_id = request.POST['todo_list_id']
    todo_list = TodoList.objects.get(id = todo_list_id)
    todo_list.delete()
    return redirect('indexname')

def delete_todo_item(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(id = todo_item_id)
    todo_item.delete()
    return redirect('indexname')