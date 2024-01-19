# Generated by Django 5.0.1 on 2024-01-19 19:05

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
                ('telefone', models.CharField(max_length=13)),
                ('endereco', models.CharField(max_length=500)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=9)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=13)),
                ("endereco", models.CharField(max_length=254)),
                ("complemento", models.CharField(max_length=50)),
                ("bairro", models.CharField(max_length=100)),
                ("cep", models.CharField(max_length=9)),
            ],
        ),
    ]
