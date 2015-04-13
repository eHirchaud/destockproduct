# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date_start', models.DateTimeField(auto_now_add=True, verbose_name="Date d'action")),
                ('action_description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('ref', models.CharField(max_length=50)),
                ('real_cost', models.IntegerField()),
                ('reduce_cost', models.IntegerField()),
                ('nb_react_by_samples', models.IntegerField()),
                ('conditionement_nombre', models.DecimalField(decimal_places=2, max_digits=5)),
                ('conditionement_type', models.CharField(max_length=15)),
                ('reac_by_sample', models.DecimalField(decimal_places=2, max_digits=5)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lots',
            fields=[
                ('product_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, auto_created=True, to='orga_run.Product')),
                ('current_stock', models.IntegerField(verbose_name='Nombre de réactions restantes')),
                ('code_fabricant', models.CharField(max_length=15)),
                ('code_tmpi', models.CharField(max_length=10)),
                ('n_lot', models.CharField(max_length=20, null=True)),
                ('open_date', models.DateTimeField(verbose_name="Date d'ouverture", auto_now=True)),
                ('peremption_date', models.DateTimeField(verbose_name='Date de péremption', null=True)),
                ('manip', models.ManyToManyField(to='orga_run.Manip')),
            ],
            options={
            },
            bases=('orga_run.product',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('acro', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=8)),
                ('client', models.CharField(max_length=50)),
                ('date_start', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('projects', models.ManyToManyField(to='orga_run.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('manips', models.ManyToManyField(to='orga_run.Manip')),
                ('project', models.ForeignKey(to='orga_run.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StepProto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('reac_by_samples', models.DecimalField(decimal_places=2, max_digits=5)),
                ('reac_by_manip', models.DecimalField(decimal_places=2, max_digits=5)),
                ('manip', models.ForeignKey(to='orga_run.Manip')),
                ('products', models.ForeignKey(to='orga_run.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='run',
            name='samples',
            field=models.ManyToManyField(to='orga_run.Sample'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lots',
            name='samples',
            field=models.ManyToManyField(to='orga_run.Sample'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='lot',
            field=models.ForeignKey(to='orga_run.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='protocole',
            field=models.ForeignKey(to='orga_run.StepProto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionproject',
            name='project',
            field=models.ForeignKey(to='orga_run.Project'),
            preserve_default=True,
        ),
    ]
