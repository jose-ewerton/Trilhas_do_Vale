from django.contrib import admin

# importando classes
from .models import Administrador,Usuario, Local, Localcategoria, Usuarioavalialocal, Usuariolocal, Avaliacaosite


admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Local)
admin.site.register(Localcategoria)
admin.site.register(Usuarioavalialocal)
admin.site.register( Usuariolocal)
admin.site.register(Avaliacaosite)