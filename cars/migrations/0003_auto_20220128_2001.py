# Generated by Django 3.2.9 on 2022-01-28 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_carbrand_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='model_id',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='office_id',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='carmodel',
            old_name='brand_id',
            new_name='brand',
        ),
    ]