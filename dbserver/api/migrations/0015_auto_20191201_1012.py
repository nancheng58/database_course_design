# Generated by Django 2.2.6 on 2019-12-01 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20191130_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
