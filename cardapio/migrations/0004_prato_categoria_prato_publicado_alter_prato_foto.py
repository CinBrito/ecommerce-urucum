# Generated by Django 5.0.1 on 2024-01-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cardapio", "0003_remove_prato_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="prato",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("PRATOS FUNDAMENTAIS", "Pratos Fundamentais"),
                    ("CUMBUCAS", "Cumbuca"),
                    ("ENSOPADOS", "Ensopados"),
                    ("SALTEADOS", "Salteados"),
                    ("SALADAS", "Saladas"),
                ],
                default="",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="prato",
            name="publicado",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="prato",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d/"),
        ),
    ]
