# Generated by Django 2.0.5 on 2019-12-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_auto_20191219_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='date_of_birth',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
