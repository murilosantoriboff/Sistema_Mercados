from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from .forms import ProdutoModelForm
from django.shortcuts import redirect

def home(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        return render(request, 'home.html', {'produtos':produtos})
    else:
        return HttpResponse('Erro na pagina')

def criar_produto(request):
    if request.method == 'GET':
        form = ProdutoModelForm()
        return render(request, 'form.html', {'form':form})
    else:
        form = ProdutoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/actions_basic/')
        else:
            form = ProdutoModelForm()
            return render(request, 'form.html', {'form':form})

def excluir_produto(request, id):
    try:
        produto = Produto.objects.get(id=id)
        produto.delete()
        return redirect('/actions_basic/')
    except:
        return HttpResponse('Erro na hora de excluir o cliente')

def editar_produto(request, id):
    try:
        if request.method == 'GET':
            produto = Produto.objects.get(id=id)
            form = ProdutoModelForm(instance=produto)
            return render(request, 'form.html', {'produto':produto, 'form':form})
        elif request.method == 'POST':
            produto = Produto.objects.get(id=id)
            form = ProdutoModelForm(request.POST, instance=produto)
            if form.is_valid():
                form.save()
                return redirect('/actions_basic/')
            else:
                form = ProdutoModelForm()
                return render(request, 'form.html', {'form':form})
        
    except:
        return HttpResponse('Erro na hora de editar um produto')