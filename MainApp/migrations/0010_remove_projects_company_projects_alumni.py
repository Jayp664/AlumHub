# Generated by Django 5.0.3 on 2024-09-05 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_rename_alum_alumni_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='company',
        ),
        migrations.AddField(
            model_name='projects',
            name='alumni',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainApp.alumni'),
            preserve_default=False,
        ),
    ]
