from django.shortcuts import render,redirect
from . models import Aluno
from . forms import AlunoForm


def home(request):
    return render(request,'home.html')

def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/list.html',{'alunos':alunos})

def aluno_show(request,id):
    aluno = Aluno.objects.get(pk=id)
    return render(request, 'aluno/show.html',{'aluno':aluno})

def aluno_delete(request,id):
    Aluno.objects.get(pk=id).delete()
    return redirect('/aula/aluno/')

def editar(request,id):
    if(request.method=='POST'):
        aluno = Aluno.objects.get(pk=id)
        form = AlunoForm(request.POST ,instance = aluno)
        if form.is_valid():
            form.save()
            return redirect('/aula/aluno/')
        else:
            return render(request,'aluno/editar.html',{'form':form, 'id':id})        
    else:
        aluno = Aluno.objects.get(pk=id)
        form = AlunoForm(instance = aluno)
        return render(request,'aluno/editar.html',{'form':form,'id':id})

def create(request):
    if(request.method=='POST'):
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/aula/aluno/')
        else:
            return render(request,'aluno/form.html',{'form':form})        
    else:
        form = AlunoForm()
        return render(request,'aluno/form.html',{'form':form})