# Generated by Django 2.2 on 2021-04-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PickupApp', '0006_auto_20210418_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='link',
            field=models.TextField(default='the link go here'),
            preserve_default=False,
        ),
    ]