# Generated by Django 3.0.8 on 2020-07-05 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200705_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=20000000)),
                ('projects', models.CharField(max_length=20000000)),
                ('achievements', models.CharField(max_length=20000000, null=True)),
                ('skills', models.CharField(max_length=20000000, null=True)),
                ('fieldOfInterest', models.CharField(max_length=20000000, null=True)),
                ('relevantCourses', models.CharField(max_length=20000000, null=True)),
                ('extraCurricular', models.CharField(max_length=20000000, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
