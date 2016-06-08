# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-06 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_similar_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=350, verbose_name=b'Title')),
                ('value', models.CharField(max_length=450, verbose_name=b'value')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='FeaturesProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('value', models.CharField(max_length=10000, verbose_name=b'value')),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features_group_features', to='catalog.Features')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.Product')),
            ],
            options={
                'verbose_name': 'Features Product',
                'verbose_name_plural': 'Features Products',
            },
        ),
        migrations.CreateModel(
            name='GroupsFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=1000, verbose_name=b'Title')),
            ],
            options={
                'verbose_name': 'Group Feature',
                'verbose_name_plural': 'Groups Features',
            },
        ),
        migrations.AddField(
            model_name='features',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_features', to='catalog.GroupsFeatures'),
        ),
    ]