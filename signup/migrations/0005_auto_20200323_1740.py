# Generated by Django 3.0.4 on 2020-03-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20200323_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='janta',
            name='gender',
            field=models.CharField(choices=[('male', '  Male'), ('female', 'Female')], max_length=10),
        ),
    ]
