# Generated by Django 3.2.4 on 2021-06-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workoutapp', '0008_event_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='event',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='content',
            name='set_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='content',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
