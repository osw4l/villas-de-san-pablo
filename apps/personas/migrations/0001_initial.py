# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 18:47
from __future__ import unicode_literals

import apps.personas.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_casa', models.CharField(max_length=30, unique=True)),
                ('numero_casa', models.SmallIntegerField()),
                ('numero_telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('numero_telefono_2', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Manzana',
                'verbose_name_plural': 'Manzanas',
            },
            bases=(apps.personas.models.CantidadPersonas, models.Model),
        ),
        migrations.CreateModel(
            name='ExperienciaLaboralPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Experiencia laboral')),
                ('lapso_de_tiempo', models.CharField(choices=[('DIAS', 'DIAS'), ('SEMANAS', 'SEMANAS'), ('MESES', 'MESES'), ('AÑOS', 'AÑOS')], max_length=20)),
                ('cantidad_de_tiempo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FormacionComplementariaPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GradoEscolaridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grado_escolaridad', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Grado de escolaridad',
                'verbose_name_plural': 'Grados de escolaridad',
            },
            bases=(apps.personas.models.CantidadPersonas, models.Model),
        ),
        migrations.CreateModel(
            name='Manzana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_manzana', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'Manzana',
                'verbose_name_plural': 'Manzanas',
            },
            bases=(apps.personas.models.CantidadPersonas, models.Model),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=20, unique=True)),
                ('tipo_documento_identificacion', models.CharField(choices=[('REGISTRO CIVIL', 'REGISTRO CIVIL'), ('TARJETA DE IDENTIDAD', 'TARJETA DE IDENTIDAD'), ('CEDULA DE CIUDADANIA', 'CEDULA DE CIUDADANIA'), ('CEDULA DE EXTRANGERIA', 'CEDULA DE EXTRANGERIA'), ('PASAPORTE', 'PASAPORTE')], max_length=30)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=12)),
                ('estado_civil', models.CharField(choices=[('SOLTERO/A', 'SOLTERO/A'), ('CASADO/A', 'CASADO/A'), ('VIUDO/A', 'VIUDO/A'), ('UNION LIBRE', 'UNION LIBRE')], max_length=20)),
                ('edad', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('telefono_1', models.CharField(blank=True, max_length=12, null=True)),
                ('telefono_2', models.CharField(blank=True, max_length=12, null=True)),
                ('telefono_3', models.CharField(blank=True, max_length=12, null=True)),
                ('fecha_de_registro', models.DateField(auto_now_add=True)),
                ('fecha_ingreso', models.DateField()),
                ('tiene_empleo', models.BooleanField(default=False)),
                ('origen_ingreso', models.CharField(max_length=50)),
                ('ingreso_promedio_mensual', models.PositiveIntegerField(blank=True, null=True)),
                ('ingreso_promedio_familiares', models.PositiveIntegerField(blank=True, null=True)),
                ('ingreso_promedio_mensuales', models.PositiveIntegerField(blank=True, null=True)),
                ('vulnerabilidad', models.BooleanField(default=False)),
                ('hoja_de_vida', models.FileField(blank=True, null=True, upload_to='cv')),
                ('cv_last_update', models.DateField(blank=True, editable=False, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('casa', smart_selects.db_fields.ChainedForeignKey(chained_field='manzana', chained_model_field='manzana', on_delete=django.db.models.deletion.CASCADE, to='personas.Casa')),
                ('grado_escolaridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.GradoEscolaridad')),
                ('manzana', smart_selects.db_fields.ChainedForeignKey(chained_field='tipo_manzana', chained_model_field='tipo_manzana', on_delete=django.db.models.deletion.CASCADE, to='personas.Manzana')),
            ],
        ),
        migrations.CreateModel(
            name='TipoFormacionComplementaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True, verbose_name='Nombre del tipo de formacion complementaria')),
            ],
            options={
                'verbose_name': 'Tipo de formacion complementaria',
                'verbose_name_plural': 'Tipos de formacion complementaria',
            },
        ),
        migrations.CreateModel(
            name='TipoManzana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_manzana', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Manzana',
                'verbose_name_plural': 'Tipos de Manzana',
            },
            bases=(apps.personas.models.CantidadPersonas, models.Model),
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_vivienda', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Vivienda',
                'verbose_name_plural': 'Tipos de Vivienda',
            },
            bases=(apps.personas.models.CantidadPersonas, models.Model),
        ),
        migrations.CreateModel(
            name='TituloGrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_titulo', models.CharField(max_length=50, unique=True)),
                ('grado_escolaridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.GradoEscolaridad')),
            ],
            options={
                'verbose_name': 'Titulo Grado',
                'verbose_name_plural': 'Titulo Grados',
            },
            bases=(apps.personas.models.CantidadPersonas, models.Model),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_manzana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.TipoManzana'),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_vivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.TipoVivienda'),
        ),
        migrations.AddField(
            model_name='persona',
            name='titulo_grado',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='grado_escolaridad', chained_model_field='grado_escolaridad', on_delete=django.db.models.deletion.CASCADE, to='personas.TituloGrado'),
        ),
        migrations.AddField(
            model_name='manzana',
            name='tipo_manzana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.TipoManzana'),
        ),
        migrations.AddField(
            model_name='formacioncomplementariapersona',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_b', to='personas.Persona'),
        ),
        migrations.AddField(
            model_name='formacioncomplementariapersona',
            name='tipo_formacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.TipoFormacionComplementaria'),
        ),
        migrations.AddField(
            model_name='experiencialaboralpersona',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_a', to='personas.Persona'),
        ),
        migrations.AddField(
            model_name='casa',
            name='numero_manzana',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='tipo_manzana', chained_model_field='tipo_manzana', on_delete=django.db.models.deletion.CASCADE, to='personas.Manzana'),
        ),
        migrations.AddField(
            model_name='casa',
            name='tipo_manzana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.TipoManzana'),
        ),
        migrations.AddField(
            model_name='casa',
            name='tipo_vivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.TipoVivienda'),
        ),
        migrations.AlterUniqueTogether(
            name='manzana',
            unique_together=set([('numero_manzana', 'tipo_manzana')]),
        ),
    ]
