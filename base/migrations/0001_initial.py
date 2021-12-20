# Generated by Django 3.2.10 on 2021-12-20 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('orgaopublico', models.CharField(db_column='orgaoPublico', max_length=40)),
                ('senha', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('senha', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Usuariopergunta',
            fields=[
                ('idusuario', models.OneToOneField(db_column='idUsuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='base.usuario')),
                ('perguntapersonalizada', models.CharField(db_column='perguntaPersonalizada', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('foto', models.ImageField(upload_to='locais/')),
                ('localizacaoexata', models.CharField(db_column='localizacaoExata', max_length=60)),
                ('descricao', models.TextField()),
                ('categorias', models.ManyToManyField(to='base.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacaosite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True, null=True)),
                ('nota', models.PositiveIntegerField(blank=True, null=True)),
                ('idusuario', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.DO_NOTHING, to='base.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuariolocal',
            fields=[
                ('idusuario', models.OneToOneField(db_column='idUsuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='base.usuario')),
                ('idlocal', models.ForeignKey(db_column='idLocal', on_delete=django.db.models.deletion.DO_NOTHING, to='base.local')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarioavalialocal',
            fields=[
                ('comentario', models.TextField(blank=True, null=True)),
                ('nota', models.PositiveIntegerField(blank=True, null=True)),
                ('idusuario', models.OneToOneField(db_column='idUsuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='base.usuario')),
                ('idlocal', models.ForeignKey(db_column='idLocal', on_delete=django.db.models.deletion.DO_NOTHING, to='base.local')),
            ],
        ),
    ]
