# Generated by Django 2.2.4 on 2019-09-27 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tokenlist',
            name='Contractadress',
        ),
    ]
