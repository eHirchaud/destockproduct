# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orga_run', '0003_auto_20150414_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='conditionement_nombre',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='nb_react_by_samples',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='real_cost',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='reduce_cost',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
