from django.shortcuts import render, redirect
from todoapp.models import Todo

# Create your views here.


def collectTask(request):
    all_todos = Todo.objects.all()
    if request.method == "POST":
        mytask = request.POST.get('mytask')
        t = Todo(task=mytask)
        t.save()

    context = {
        'all_todos': all_todos
    }
    return render(request, "todo.html", context)


def deleteOneTask(request, id):
    onetodo = Todo.objects.get(id=id)
    onetodo.delete()
    return redirect("/task")
