# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type_field', models.TextField(null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('movie', models.ForeignKey(to='website.Movie', blank=True, null=True)),
            ],
            options={
                'db_table': 'Projections',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('username', models.TextField(null=True, blank=True)),
                ('row', models.IntegerField(null=True, blank=True)),
                ('col', models.IntegerField(null=True, blank=True)),
                ('projection', models.ForeignKey(to='website.Projection', blank=True, null=True)),
            ],
            options={
                'db_table': 'Reservations',
            },
        ),
    ]
