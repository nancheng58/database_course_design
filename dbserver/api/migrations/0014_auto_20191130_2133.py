# Generated by Django 2.2.6 on 2019-11-30 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20191128_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=233666, on_delete=django.db.models.deletion.CASCADE, to='api.Teacher'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='admin',
            name='usertype',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Elective',
            fields=[
                ('elective_id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
            options={
                'verbose_name': '选课',
                'verbose_name_plural': '选课',
            },
        ),
    ]
