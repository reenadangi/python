# Generated by Django 2.2.7 on 2019-12-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbook', '0004_auto_20191212_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
