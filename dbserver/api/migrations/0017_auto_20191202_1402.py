# Generated by Django 2.2.6 on 2019-12-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20191201_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='name',
            new_name='content',
        ),
        migrations.AddField(
            model_name='award',
            name='flag',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
