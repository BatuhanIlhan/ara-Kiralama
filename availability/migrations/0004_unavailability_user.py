# Generated by Django 3.2.9 on 2022-03-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('availability', '0003_rename_car_id_unavailability_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='unavailability',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
    ]
