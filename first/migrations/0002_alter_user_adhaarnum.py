# Generated by Django 4.0.6 on 2022-07-15 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='adhaarnum',
            field=models.IntegerField(max_length=12),
        ),
    ]
