# Generated by Django 2.2.4 on 2019-11-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20191112_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='requestbuytoken',
        ),
    ]
