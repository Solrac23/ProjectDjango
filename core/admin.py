from django.contrib import admin

# Register your models here.
from .models import Product, Client

class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'preco',
        'estoque'
    )

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sobrenome',
        'email'
    )

admin.site.register(Product, ProdutoAdmin)
admin.site.register(Client, ClienteAdmin)