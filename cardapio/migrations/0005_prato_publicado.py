# Generated by Django 5.0.1 on 2024-01-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0004_prato_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]