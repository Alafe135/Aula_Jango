from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefas
from .forms import Tarefaform
# Create your views here.

def listaTarefa(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')

    return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})

def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':tarefa})

def novaTarefa(request):

    if request.method == 'POST':
        form = Tarefaform(request.POST)

        if form.is_valid():
            tarefa = form.save()
            tarefa.save()
            return redirect('/')
    
    else:
        form = Tarefaform()
        return render(request, 'Tarefas/addTarefa.html', {'form':form})
    
def editTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = Tarefaform(request.POST, instance=tarefa)
    if (request.method == 'POST'):
        form = Tarefaform(request.POST, instance=tarefa)
        if (form.is_valid()):
            tarefa.save()
            return redirect('/')
        
        else:
            return render (request, 'tarefas/editTarefa.html',{'form':form, 'tarefa': tarefa})
        
    else:
        return render(request, 'tarefas/editTarefa.html', {'form':form , 'tarefa': tarefa})

def deleteTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    tarefa.delete()
    return redirect('/')
            
