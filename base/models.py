from django.db import models

class Administrador(models.Model):
    name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=45)
    orgaopublico = models.CharField(db_column='orgaoPublico', max_length=40) # Field name made lowercase.
    senha = models.CharField(max_length=12)

class Meta:
    managed = False
    db_table = 'Administrador'

def __str__(self):
        
        return "{} ({})" .format(self.nome, self.orgaopublico)



class Avaliacaosite(models.Model):
    comentario = models.TextField(blank=True, null=True)
    nota = models.PositiveIntegerField(blank=True, null=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario') # Field name made lowercase.

class Meta:
    managed = False
    db_table = 'AvaliacaoSite'

    def __str__(self):
        
        return "{} ({})" .format(self.usuario)



class Local(models.Model):
    nome = models.CharField(max_length=40)
    foto = models.ImageField()
    localizacaoexata = models.CharField(db_column='localizacaoExata', max_length=60) # Field name made lowercase.
    descricao = models.TextField()

class Meta:
    managed = False
    db_table = 'Local'

def __str__(self):
        
        return "{} ({})" .format(self.nome, self.foto)



class Localcategoria(models.Model):
    idlocal = models.OneToOneField(Local, models.DO_NOTHING, db_column='idLocal', primary_key=True) # Field name made lowercase.
    categoria = models.CharField(max_length=30)

class Meta:
    managed = False
    db_table = 'LocalCategoria'
    unique_together = (('idlocal', 'categoria'),)

def __str__(self):
        
    return "{} ({})" .format(self.idlocal, self.categoria)



class Usuario(models.Model):
    nome = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=45)
    senha = models.CharField(max_length=12)
    

class Meta:
    managed = False
    db_table = 'Usuario'
    
def __str__(self):
        
        return "{} ({})" .format(self.nome, self.email)

#def __repr__(self):
        
#       return "{} ({})" .format(self.nome, self.email)


# no admin aparece Usuario object (3).
# utilize o método __repr__ para formatar o nome do objeto que aparece no admin.

class Usuarioavalialocal(models.Model):
    comentario = models.TextField(blank=True, null=True)
    nota = models.PositiveIntegerField(blank=True, null=True)
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='idUsuario', primary_key=True) # Field name made lowercase.
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idLocal') # Field name made lowercase.

class Meta:
    managed = False
    db_table = 'UsuarioAvaliaLocal'
    unique_together = (('idusuario', 'idlocal'),)

    def __str__(self):
        
        return "{} ({})" .format(self.idusuario, self.idlocal)

class Usuariolocal(models.Model):
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='idUsuario', primary_key=True) # Field name made lowercase.
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idLocal') # Field name made lowercase.

class Meta:
    managed = False
    db_table = 'UsuarioLocal'
    unique_together = (('idusuario', 'idlocal'),)


    def __str__(self):
        
        return "{} ({})" .format(self.idusuario, self.idlocal)



class Usuariopergunta(models.Model):
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='idUsuario', primary_key=True) # Field name made lowercase.
    perguntapersonalizada = models.CharField(db_column='perguntaPersonalizada', max_length=25) # Field name made lowercase.

class Meta:
    managed = False
    db_table = 'UsuarioPergunta'
    unique_together = (('idusuario', 'perguntapersonalizada'),)

def __str__(self):
        
        return "{} ({})" .format(self.idusuario)