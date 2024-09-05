# Generated by Django 5.0.3 on 2024-09-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_seminar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='passyear',
        ),
        migrations.AddField(
            model_name='alumni',
            name='endyear',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumni',
            name='startyear',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
