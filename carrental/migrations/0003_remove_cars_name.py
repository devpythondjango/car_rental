# Generated by Django 4.2.11 on 2024-05-01 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0002_remove_cars_carbrends_carmodels_carbrends_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='name',
        ),
    ]
