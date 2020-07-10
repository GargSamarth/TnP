# Generated by Django 3.0.8 on 2020-07-10 11:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20200710_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='achievements',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='address',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='education',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='email',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='extraCurricular',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='name',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='relevantCourses',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='year',
        ),
        migrations.AddField(
            model_name='resume',
            name='resume',
            field=models.FileField(null=True, upload_to='images/Resume', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
