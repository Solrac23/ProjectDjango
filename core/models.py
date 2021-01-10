from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    
    preco = models.DecimalField('Preço', 
    decimal_places=2, 
    max_digits=8
    )
    
    estoque = models.IntegerField('Quantidade em estoque')
    
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.name} {self.sobrenome}'