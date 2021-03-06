# Generated by Django 3.0.2 on 2020-01-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=255, verbose_name='CPF')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('NB', 'Não-binário'), ('O', 'Outros')], max_length=255, verbose_name='Gênero')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
