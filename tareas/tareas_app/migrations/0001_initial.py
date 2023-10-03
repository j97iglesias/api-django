# Generated by Django 4.2.5 on 2023-09-12 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proyecto",
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
                ("nombre", models.CharField(max_length=55)),
                ("descripcion", models.TextField()),
                ("fecha_inicio", models.DateField()),
                ("fecha_finalizacioon", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
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
                ("nombre", models.CharField(max_length=55)),
                ("correo_electronico", models.CharField(max_length=100)),
                ("contrasena", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tarea",
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
                ("nombre", models.CharField(max_length=55)),
                ("descripcion", models.CharField(max_length=100)),
                ("fecha_vencimiento", models.DateField()),
                ("estado", models.BooleanField(default=False)),
                (
                    "idproyecto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tareas_app.proyecto",
                    ),
                ),
                (
                    "idusuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tareas_app.usuario",
                    ),
                ),
            ],
        ),
    ]