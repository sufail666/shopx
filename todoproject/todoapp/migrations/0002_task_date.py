# Generated by Django 3.2.9 on 2021-11-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-10-24'),
            preserve_default=False,
        ),
    ]
