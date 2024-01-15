# Generated by Django 5.0.1 on 2024-01-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=50),
        ),
    ]