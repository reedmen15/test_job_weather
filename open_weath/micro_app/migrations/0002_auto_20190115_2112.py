# Generated by Django 2.1.5 on 2019-01-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
