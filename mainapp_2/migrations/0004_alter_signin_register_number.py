# Generated by Django 3.2.5 on 2021-07-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_2', '0003_signin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='Register_number',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
