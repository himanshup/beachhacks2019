# Generated by Django 2.2 on 2019-04-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190421_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='beach_id',
            field=models.CharField(max_length=255),
        ),
    ]
