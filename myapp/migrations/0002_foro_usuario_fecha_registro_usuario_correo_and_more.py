# Generated by Django 5.0.1 on 2024-10-31 14:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foro', models.CharField(max_length=100, verbose_name='Foro')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('Tema', models.CharField(max_length=100, verbose_name='Tema')),
                ('fechaCreacion', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='Fecha_Registro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default='example@example.com', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default='user', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=100, verbose_name='Nombre de usuario'),
        ),
        migrations.CreateModel(
            name='Foro_Participacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaParticipacion', models.DateField()),
                ('foro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.foro')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Informe_Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('FechaSubida', models.DateField()),
                ('Id_reporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.foro')),
            ],
        ),
    ]
