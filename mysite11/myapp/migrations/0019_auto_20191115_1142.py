# Generated by Django 2.2.4 on 2019-11-15 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20191113_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='requesttokenbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('one_tokenprice', models.FloatField(default=0)),
                ('requesttoken_num', models.FloatField(default=0)),
                ('buyer_account', models.CharField(blank=True, max_length=200)),
                ('seller_account', models.CharField(blank=True, max_length=200)),
                ('sellertotaltoken', models.FloatField(default=0)),
                ('company_code', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='requestbuytoken',
        ),
    ]
