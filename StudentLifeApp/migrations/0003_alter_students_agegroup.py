# Generated by Django 4.0.5 on 2022-06-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentLifeApp', '0002_alter_students_agegroup_alter_students_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='ageGroup',
            field=models.CharField(choices=[('Younger than 17 years', 'Younger than 17 years'), ('17 to 20 years', '17 to 20 years'), ('21 a 23 years', '21 a 23 years'), ('Older than 23 years', 'Older than 23 years')], max_length=40),
        ),
    ]
