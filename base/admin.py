from django.contrib import admin

# importando classes
from .models import  Categoria, Local


admin.site.register(Local)
admin.site.register(Categoria)
