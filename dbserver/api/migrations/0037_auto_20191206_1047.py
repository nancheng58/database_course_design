# Generated by Django 2.2.6 on 2019-12-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20191206_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elective',
            name='score',
            field=models.IntegerField(blank=True, default=80),
            preserve_default=False,
        ),
    ]
