# Generated by Django 2.2 on 2021-04-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PickupApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Age',
            field=models.IntegerField(),
        ),
    ]