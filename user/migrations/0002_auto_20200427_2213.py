# Generated by Django 3.0.5 on 2020-04-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.IntegerField(max_length=11),
        ),
    ]
