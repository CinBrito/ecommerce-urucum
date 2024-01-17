# Generated by Django 5.0.1 on 2024-01-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(max_length=150)),
                ('endereco', models.CharField(max_length=500)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.IntegerField(max_length=8)),
            ],
        ),
    ]