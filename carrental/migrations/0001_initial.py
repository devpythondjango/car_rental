# Generated by Django 4.2.11 on 2024-05-01 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_konditsioner', models.BooleanField()),
                ('is_gps', models.BooleanField()),
                ('is_bagaj', models.BooleanField()),
                ('is_musiqa', models.BooleanField()),
                ('is_kamar', models.BooleanField()),
                ('is_audio_kiritsh', models.BooleanField()),
                ('is_bluethooth', models.BooleanField()),
                ('is_uzoq_masofa', models.BooleanField()),
                ('is_uxlash_stoli', models.BooleanField()),
                ('is_kalit_plut', models.BooleanField()),
                ('is_bortli_kompyuter', models.BooleanField()),
                ('name', models.CharField(blank=True, max_length=155, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/car/image')),
                ('kilometers', models.IntegerField(blank=True, null=True)),
                ('mator', models.CharField(blank=True, max_length=50, null=True)),
                ('sat_down', models.IntegerField(blank=True, null=True)),
                ('baggage', models.CharField(blank=True, max_length=50, null=True)),
                ('fuel', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('carprice', models.DateTimeField(auto_now_add=True)),
                ('carbrends', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrental.carbrends')),
                ('carmodels', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrental.carmodels')),
                ('caryear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrental.caryear')),
            ],
        ),
    ]
