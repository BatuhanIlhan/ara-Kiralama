# Generated by Django 3.2.9 on 2022-01-22 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
    ]
