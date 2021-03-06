# Generated by Django 3.0.7 on 2020-07-01 13:54

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('name', models.CharField(default='ABC', max_length=120, primary_key=True, serialize=False)),
                ('websiteLink', models.CharField(max_length=120)),
                ('hrDetails', models.CharField(max_length=20000)),
                ('address', models.CharField(max_length=20000)),
                ('emailId', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('mobileNumber', models.IntegerField()),
                ('sector', models.CharField(blank=True, default='', max_length=2000, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('category', models.CharField(blank=True, default='', max_length=2000, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('jobDesignation', models.CharField(max_length=120)),
                ('jobType', models.CharField(blank=True, default='', max_length=200, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('workLocation', models.CharField(max_length=1000)),
                ('tentativeDOJ', models.DateField()),
                ('roundsDetails', models.CharField(blank=True, default='', max_length=20000, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('numberOfRounds', models.IntegerField()),
                ('otherInfo', models.CharField(max_length=1000)),
                ('salaryDetails_btech', models.CharField(max_length=1000)),
                ('salaryDetails_mtech', models.CharField(max_length=1000)),
                ('salaryDetails_otherPG', models.CharField(max_length=1000)),
                ('salaryDetails_PhD', models.CharField(max_length=1000)),
                ('trainingPeriod', models.IntegerField(default=0)),
                ('stipulatedBond', models.IntegerField(default=0)),
                ('stipendDetails_BTech', models.CharField(max_length=1000)),
                ('stipendDetails_MTech', models.CharField(max_length=1000)),
                ('stipendDetails_OtherPG', models.CharField(max_length=1000)),
                ('duration_UG', models.CharField(max_length=1000)),
                ('duration_PG', models.CharField(max_length=1000)),
            ],
        ),
    ]
