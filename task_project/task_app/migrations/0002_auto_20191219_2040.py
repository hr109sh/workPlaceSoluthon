# Generated by Django 2.0.5 on 2019-12-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]