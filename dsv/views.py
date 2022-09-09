from django.shortcuts import render, get_object_or_404, redirect
from .models import Processo, Equipamento
from .forms import ProcessoForm, EquipamentoForm

def home(request):
    return render(request, 'home.html')


def atualizar_processo(request, id):
    processo = get_object_or_404(Processo, pk=id)
    form = ProcessoForm(request.POST or None, instance=processo)

    if form.is_valid():
        form.save()
        return redirect('lista_processos')
    
    return render(request, 'processo_form.html', {'form': form})

def lista_processo(request):
    processo = Processo.objects.all()
    return render(request, 'lista_processo.html', {'processo': processo})


def delete_processos(request, id):
    processo = get_object_or_404(Processo, pk=id)
    # form = ProcessoForm(request.POST or None, instance=processo)

    if request.method == 'POST':
        processo.delete()
        return redirect('lista_processos')

    return render(request, 'delete_processo_confirmar.html', {'processo': processo})

    
def criar_processos(request):
    form = ProcessoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_processos')

    return render(request, 'criar_processo.html', {'form': form})


def detalhes_processo(request, id):
    processo = get_object_or_404(Processo, pk=id)
    form = ProcessoForm(request.POST or None, instance=processo)

    equipamentos = Equipamento.objects.filter(processo_id=id)
    # equipamento = get_object_or_404(Equipamento, pk=id)
    

    return render(request, 'detalhes_processo.html', {'form': form, 'equipamentos': equipamentos})


def lista_equipamentos(request, id):
    equipamentos = Equipamento.objects.filter(processo_id=id)
    return render(request, 'lista_equipamentos.html', {'equipamentos': equipamentos})
    

def atualizar_equipamentos(request, id):
    equipamentos = get_object_or_404(Equipamento, pk=id)
    form = EquipamentoForm(request.POST or None, instance=equipamentos)

    if form.is_valid():
        form.save()
        return redirect('lista_equipamentos')

    return render(request, 'equipamento_form.html', {'form': form})

def delete_equipamentos(request, id):
    equipamentos = get_object_or_404(Equipamento, pk=id)
   
    if request.method == 'POST':
        equipamentos.delete()
        return redirect('lista_equipamentos')

    return render(request, 'delete_equipamento_confirmar.html', {'equipamentos':equipamentos})

    
def criar_equipamentos(request):
    form = EquipamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_equipamentos')

    return render(request, 'criar_equipamentos.html', {'form': form})

def detalhes_equipamentos(request, id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    form = EquipamentoForm(request.POST or None, instance=equipamento)

    return render(request, 'detalhes_equipamentos.html', {'form': form})
