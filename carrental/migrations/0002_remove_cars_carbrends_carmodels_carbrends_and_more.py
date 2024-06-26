# Generated by Django 4.2.11 on 2024-05-01 09:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='carbrends',
        ),
        migrations.AddField(
            model_name='carmodels',
            name='carbrends',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrental.carbrends'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
