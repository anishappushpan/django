# Generated by Django 3.0 on 2020-01-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regapp', '0003_auto_20200107_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atta',
            name='fourthp',
            field=models.CharField(blank='True', default='', max_length=10, null='True'),
        ),
        migrations.AlterField(
            model_name='atta',
            name='thirdp',
            field=models.CharField(blank='True', default='', max_length=10, null='True'),
        ),
    ]
