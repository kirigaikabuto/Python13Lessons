# Generated by Django 3.1.7 on 2021-03-20 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
