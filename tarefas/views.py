from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefas
from .forms import Tarefaform
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def listaTarefa(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at'). filter(usuario=request.user)

    return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})

@login_required
def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':tarefa})

@login_required
def novaTarefa(request):

    if request.method == 'POST':
        form = Tarefaform(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('/')
    
    else:
        form = Tarefaform()
        return render(request, 'Tarefas/addTarefa.html', {'form':form})
    
@login_required
def editTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = Tarefaform(instance=tarefa)

    if (request.method == 'POST'):
        form = Tarefaform(request.POST, instance=tarefa)
        if (form.is_valid()):
            tarefa.save()
            return redirect('/')
        
        else:
            return render (request, 'tarefas/editTarefa.html',{'form':form, 'tarefa': tarefa})
        
    else:
        return render(request, 'tarefas/editTarefa.html', {'form':form , 'tarefa': tarefa})
    
@login_required
def deleteTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    tarefa.delete()
    return redirect('/')
            
