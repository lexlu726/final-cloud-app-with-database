# Generated by Django 3.1.3 on 2023-08-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='choices',
        ),
        migrations.AddField(
            model_name='submission',
            name='choice_List',
            field=models.CharField(default='', max_length=200),
        ),
    ]
