# Generated by Django 3.2.9 on 2022-03-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220318_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='USERNAME_FIELD',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
