# Generated by Django 3.1.3 on 2020-11-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=20)),
                ('days', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('arrival', models.CharField(max_length=20)),
                ('departure', models.CharField(max_length=20)),
            ],
        ),
    ]
