# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orga_run', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('site_web', models.URLField(blank=True)),
                ('avatar', models.ImageField(upload_to='avatar/', null=True, blank=True)),
                ('signature', models.TextField(blank=True)),
                ('inscrit_newlette', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
