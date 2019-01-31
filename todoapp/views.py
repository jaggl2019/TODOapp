from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
#from django.http import HttpResponse

from .models import TodoTBL
from .forms import TodoForm

# Create your views here.
def index(request):
    #return HttpResponse('Hola desde todoapp')
    todotbltmpdeViews = TodoTBL.objects.order_by('id')
    formtmp = TodoForm()

    context = {'todotbl_deViews' : todotbltmpdeViews, 'todo_formViews' : formtmp}

    return render(request, 'todoapp/index.html', context)

@require_POST
def addTodo(request):
    form=TodoForm(request.POST)
    print(request.POST['texto']) #texto biene de la TodoForm

    if form.is_valid():
        new_todo= TodoTBL(accion=request.POST['texto']) #texto biene de la TodoForm
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = TodoTBL.objects.get(pk=todo_id)
    todo.estado = True
    todo.save()
    #print('se dio el click') #hizo click

    return redirect('index')

def deleteCompletedTodo(request):
    TodoTBL.objects.filter(estado__exact=True).delete()
    #print('se dio el click en delete completed') #hizo click

    return redirect('index')

def deleteAllTodo(request):
    TodoTBL.objects.all().delete()

    return redirect('index')