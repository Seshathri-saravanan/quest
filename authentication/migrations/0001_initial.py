# Generated by Django 3.1.3 on 2020-11-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]