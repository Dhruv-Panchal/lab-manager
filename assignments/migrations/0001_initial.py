# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-29 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_no', models.IntegerField()),
                ('subject', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('submit_date', models.DateField()),
                ('document', models.FileField(upload_to=b'')),
            ],
        ),
    ]
