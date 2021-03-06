# Generated by Django 2.2 on 2021-05-10 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PickupApp', '0008_auto_20210418_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Quotes_posted', to='PickupApp.User')),
            ],
        ),
    ]
