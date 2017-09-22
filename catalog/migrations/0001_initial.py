# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name=b'Identificador')),
                ('craeted', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Modificado em')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name=b'Identificador')),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('price', models.DecimalField(verbose_name=b'Pre\xc3\xa7o', max_digits=8, decimal_places=2)),
                ('craeted', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Modificado em')),
                ('category', models.ForeignKey(verbose_name=b'Categoria', to='catalog.Category')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
