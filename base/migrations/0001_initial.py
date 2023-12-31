# Generated by Django 4.2.5 on 2023-09-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('mensagem', models.CharField(max_length=3000)),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pet', models.CharField(max_length=150)),
                ('telefone', models.EmailField(max_length=254)),
                ('data_reserva', models.DateField(auto_now_add=True)),
                ('observacoes', models.CharField(max_length=3000)),
            ],
        ),
    ]
