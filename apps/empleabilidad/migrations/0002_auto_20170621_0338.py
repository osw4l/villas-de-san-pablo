# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleabilidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formaciontrabajopersona',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_d', to='personas.Persona'),
        ),
        migrations.AlterField(
            model_name='vacantepersona',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_c', to='personas.Persona'),
        ),
    ]