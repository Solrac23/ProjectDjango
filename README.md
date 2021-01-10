## Comando para salvar migrations
- python manage.py makemigrations
Após você criar um model usar este comando acima.

### Comando para executara migrations
- python manage.py migrates
Esté comando irá executar toda a sua migrations.

### Comando para criar um usuário admin
- python manage.py createsuperuser
Depois de criar o seu super usuário, localize a pasta admin.py e 
importe os seus models.
Ex.: admin.site.register(Product)

#### Rotas para o template
- STATIC_URL = '/static/' # Usado durante o desenvolvimento
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Usado durante a produção
- Comando para fazer a cópia do template 'static', para o staticfiles.

##### Comando para mostrar a página staticfiles
 - pip install whitenoise gunicorn
 O whitenoiese é para mostrar a página estatica.
 O gunicorn é um servidor especifico para produção de sua aplicação
 
 E depois digite esse comando em settings.py no campo MIDDLEWARE abaixo de security:
 'whitenoise.middleware.WhiteNoiseMiddleware',