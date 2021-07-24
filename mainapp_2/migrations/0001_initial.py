# Generated by Django 3.2.5 on 2021-07-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_no', models.IntegerField()),
                ('Question', models.CharField(max_length=1000)),
                ('Answer', models.CharField(max_length=100)),
                ('Option_A', models.CharField(max_length=30)),
                ('Option_B', models.CharField(max_length=30)),
                ('Option_C', models.CharField(max_length=30)),
                ('Option_D', models.CharField(max_length=30)),
            ],
        ),
    ]