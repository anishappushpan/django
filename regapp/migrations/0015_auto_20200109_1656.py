# Generated by Django 3.0 on 2020-01-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regapp', '0014_auto_20200109_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyreg',
            name='password',
            field=models.CharField(default='', max_length=10),
        ),
    ]
