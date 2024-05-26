# Generated by Django 5.0.4 on 2024-05-25 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=20)),
                ('waktu_mulai', models.TimeField()),
                ('waktu_selesai', models.TimeField()),
                ('guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.guru')),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.matapelajaran')),
            ],
        ),
    ]
