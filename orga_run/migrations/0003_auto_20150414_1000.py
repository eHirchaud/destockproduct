# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orga_run', '0002_profil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reac_by_sample',
        ),
        migrations.AlterField(
            model_name='product',
            name='nb_react_by_samples',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='real_cost',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='reduce_cost',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
    ]
