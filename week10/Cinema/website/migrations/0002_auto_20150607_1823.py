# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='col',
            new_name='seat',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='row',
        ),
    ]
