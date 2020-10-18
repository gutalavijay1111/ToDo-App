from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo, Tag
from .forms import TodoForm

def index(request):
    complete_todo_list = Todo.objects.filter(complete__exact=True).order_by('id')
    incomplete_todo_list = Todo.objects.filter(complete__exact=False).order_by('id')

    form = TodoForm()

    context = {'complete_todo_list' : complete_todo_list,'incomplete_todo_list': incomplete_todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)



@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
        tags = request.POST.getlist('tags')
        for _ in tags:
            print(">>>>>>>>",_)
            tag = Tag.objects.get(id=_)
            new_todo.tags.add(tag)
            new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    # Todo.objects.get(pk=todo_id).delete()


    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')


def reverseTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = False
    todo.save()

    return redirect('index')
