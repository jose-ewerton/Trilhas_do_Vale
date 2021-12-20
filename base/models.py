from django.db import models


class Administrador(models.Model):
    name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=45)
    orgaopublico = models.CharField(db_column='orgaoPublico', max_length=40) # Field name made lowercase.
    senha = models.CharField(max_length=12)


    def __str__(self):
            
            return "{} ({})" .format(self.nome, self.orgaopublico)



class Avaliacaosite(models.Model):
    comentario = models.TextField(blank=True, null=True)
    nota = models.PositiveIntegerField(blank=True, null=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario') # Field name made lowercase.


    def __str__(self):
        
        return "{} ({})" .format(self.usuario)




class Categoria(models.Model):
    nome = models.CharField(unique=True, max_length=30)
    

    def __str__(self):  
            return self.nome




class Local(models.Model):
    nome = models.CharField(max_length=40)
    foto = models.ImageField(upload_to = 'locais/')
    localizacaoexata = models.CharField(db_column='localizacaoExata', max_length=60) # Field name made lowercase.
    descricao = models.TextField()
    categorias = models.ManyToManyField(Categoria)

    @staticmethod
    def getLocaisByID(id):
        if id:
            return Local.objects.filter(categorias = id)
        else:
            return Local.objects.all()


    def __str__(self):  
            return self.nome




class Usuario(models.Model):
    nome = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=45)
    senha = models.CharField(max_length=12)
    

    
    def __str__(self):
            
            return "{} ({})" .format(self.nome, self.email)



class Usuarioavalialocal(models.Model):
    comentario = models.TextField(blank=True, null=True)
    nota = models.PositiveIntegerField(blank=True, null=True)
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='idUsuario', primary_key=True) # Field name made lowercase.
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idLocal') # Field name made lowercase.


    def __str__(self):
        
        return "{} ({})" .format(self.idusuario, self.idlocal)


class Usuariolocal(models.Model):
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='idUsuario', primary_key=True) # Field name made lowercase.
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idLocal') # Field name made lowercase.


    def __str__(self):
        
        return "{} ({})" .format(self.idusuario, self.idlocal)



class Usuariopergunta(models.Model):
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='idUsuario', primary_key=True) # Field name made lowercase.
    perguntapersonalizada = models.CharField(db_column='perguntaPersonalizada', max_length=25) # Field name made lowercase.


    def __str__(self):
            
            return "{} ({})" .format(self.idusuario)