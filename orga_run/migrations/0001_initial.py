# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_start', models.DateTimeField(verbose_name="Date d'action", auto_now_add=True)),
                ('action_description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntryDestock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('count_react', models.FloatField(default=0)),
                ('cost_real', models.FloatField(default=0)),
                ('cost_reduce', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('current_stock', models.IntegerField(verbose_name='Nombre de réactions restantes')),
                ('code_fabricant', models.CharField(max_length=15)),
                ('code_tmpi', models.CharField(max_length=10)),
                ('n_lot', models.CharField(max_length=20, null=True)),
                ('open_date', models.DateTimeField(verbose_name="Date d'ouverture", auto_now=True)),
                ('peremption_date', models.DateTimeField(verbose_name='Date de péremption', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('ref', models.CharField(max_length=50)),
                ('real_cost', models.FloatField()),
                ('reduce_cost', models.FloatField()),
                ('nb_react_by_samples', models.FloatField()),
                ('conditionement_nombre', models.FloatField()),
                ('conditionement_type', models.CharField(max_length=15)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('site_web', models.URLField(blank=True)),
                ('avatar', models.ImageField(upload_to='avatar/', blank=True, null=True)),
                ('signature', models.TextField(blank=True)),
                ('inscrit_newlette', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('acro', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=8)),
                ('client', models.CharField(max_length=50)),
                ('date_start', models.DateTimeField(verbose_name='Date de création', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=20)),
                ('manips', models.ManyToManyField(to='orga_run.Manip')),
                ('project', models.ForeignKey(to='orga_run.Project', related_name='samples')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StepProto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('reac_by_sample', models.FloatField(default=0)),
                ('reac_by_manip', models.FloatField(default=0)),
                ('manip', models.ForeignKey(to='orga_run.Manip', related_name='steps_proto')),
                ('product', models.ForeignKey(to='orga_run.Product', related_name='steps_proto')),
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
            model_name='lot',
            name='manip',
            field=models.ManyToManyField(to='orga_run.Manip', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lot',
            name='product',
            field=models.ForeignKey(null=True, to='orga_run.Product', related_name='lots'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lot',
            name='samples',
            field=models.ManyToManyField(to='orga_run.Sample', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrydestock',
            name='manip',
            field=models.ForeignKey(null=True, to='orga_run.Manip', related_name='entries_destock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrydestock',
            name='product',
            field=models.ForeignKey(null=True, to='orga_run.Product', related_name='entries_destock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrydestock',
            name='project',
            field=models.ForeignKey(null=True, to='orga_run.Project', related_name='entries_destock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrydestock',
            name='run',
            field=models.ForeignKey(null=True, to='orga_run.Run', related_name='entries_destock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionproject',
            name='project',
            field=models.ForeignKey(to='orga_run.Project'),
            preserve_default=True,
        ),
    ]
