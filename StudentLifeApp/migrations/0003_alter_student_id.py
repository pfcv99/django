# Generated by Django 4.0.5 on 2022-06-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentLifeApp', '0002_auto_20220621_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
