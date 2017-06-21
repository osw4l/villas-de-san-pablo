# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import apps.emprendimiento.models
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprendimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ficha_caracterizacion', models.BooleanField(default=False)),
                ('ingreso_promedio_ventas', models.PositiveIntegerField(default=0)),
                ('ingreso_promedio_ventas_finales', models.PositiveIntegerField(default=0)),
                ('capital_semilla', models.PositiveIntegerField(default=0)),
                ('inscrito_en', models.CharField(choices=[('Fortalecimiento Empresarial', 'Fortalecimiento Empresarial'), ('Emprendimiento', 'Emprendimiento')], max_length=50)),
            ],
            options={
                'verbose_name': 'Emprendimiento',
                'verbose_name_plural': 'Emprendimientos',
            },
            bases=(models.Model, apps.emprendimiento.models.BaseUpdateUrl),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
            bases=(models.Model, apps.emprendimiento.models.BaseUpdateUrl),
        ),
        migrations.CreateModel(
            name='FortalecimientoEmpresarial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=20, null=True)),
                ('nit', models.CharField(blank=True, max_length=20, null=True)),
                ('camara_de_comercio', models.BooleanField(default=False)),
                ('emprendimiento', smart_selects.db_fields.ChainedForeignKey(chained_field='negocio', chained_model_field='negocio', on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.Emprendimiento')),
            ],
            options={
                'verbose_name': 'Fortalecimiento Empresarial',
                'verbose_name_plural': 'Fortalecimientos Empresariales',
            },
            bases=(models.Model, apps.emprendimiento.models.BaseUpdateUrl),
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona')),
            ],
            options={
                'verbose_name': 'Negocio',
                'verbose_name_plural': 'Negocios',
            },
            bases=(models.Model, apps.emprendimiento.models.BaseUpdateUrl),
        ),
        migrations.CreateModel(
            name='OportunidadComercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.Empresa')),
                ('negocio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.Emprendimiento')),
            ],
            options={
                'verbose_name': 'Oportunidad Comercial',
                'verbose_name_plural': 'Oportunidades Comerciales',
            },
            bases=(models.Model, apps.emprendimiento.models.BaseUpdateUrl),
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
            },
            bases=(models.Model, apps.emprendimiento.models.BaseUpdateUrl),
        ),
        migrations.CreateModel(
            name='TipoNegocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de negocio',
                'verbose_name_plural': 'Tipos de negocio',
            },
            bases=(models.Model, apps.emprendimiento.models.BaseUpdateUrl),
        ),
        migrations.CreateModel(
            name='TipoUnidadProductiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de unidad productiva',
                'verbose_name_plural': 'Tipos de unidades productivas',
            },
            bases=(models.Model, apps.emprendimiento.models.BaseUpdateUrl),
        ),
        migrations.AddField(
            model_name='negocio',
            name='tipo_negocio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.TipoNegocio'),
        ),
        migrations.AddField(
            model_name='fortalecimientoempresarial',
            name='negocio',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='persona', chained_model_field='propietario', on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.Negocio'),
        ),
        migrations.AddField(
            model_name='fortalecimientoempresarial',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona'),
        ),
        migrations.AddField(
            model_name='emprendimiento',
            name='negocio',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='tipo_negocio', chained_model_field='tipo_negocio', on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.Negocio'),
        ),
        migrations.AddField(
            model_name='emprendimiento',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona'),
        ),
        migrations.AddField(
            model_name='emprendimiento',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.Sector'),
        ),
        migrations.AddField(
            model_name='emprendimiento',
            name='tipo_negocio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.TipoNegocio'),
        ),
        migrations.AddField(
            model_name='emprendimiento',
            name='tipo_unidad_productova',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprendimiento.TipoUnidadProductiva'),
        ),
        migrations.AlterUniqueTogether(
            name='emprendimiento',
            unique_together=set([('persona', 'negocio')]),
        ),
    ]
