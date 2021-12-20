from django.contrib import admin

# importando classes
from .models import Administrador, Categoria, Usuario, Local, Usuarioavalialocal, Usuariolocal, Avaliacaosite


admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Usuarioavalialocal)
admin.site.register( Usuariolocal)
admin.site.register(Avaliacaosite)