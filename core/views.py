from django.shortcuts import render
from django.shortcuts import get_object_or_404 # Apresentar página não encontrada.
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import Product

def index(request):
    produtos = Product.objects.all()
    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def produto(request, pk):
    # prod = Product.objects.get(id=pk)
    prod = get_object_or_404(Product, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(
        content=template.render(), 
        content_type='text/html; charset=utf8', 
        status=404
        )

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(
        content=template.render(),
        content_type='txt/html; charset=utf8',
        status=500
    )      
