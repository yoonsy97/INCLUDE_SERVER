# Generated by Django 2.2.4 on 2019-11-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_client_info_krw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_info',
            name='KRW',
            field=models.IntegerField(default=0),
        ),
    ]
