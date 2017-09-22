# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20170921_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='craeted',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='craeted',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name=b'Slug'),
        ),
    ]
