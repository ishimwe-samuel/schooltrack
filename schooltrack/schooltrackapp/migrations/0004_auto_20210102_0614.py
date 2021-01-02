# Generated by Django 3.1.4 on 2021-01-02 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schooltrackapp', '0003_auto_20210102_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_credits',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='CompletedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_completion', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schooltrackapp.course')),
            ],
        ),
    ]