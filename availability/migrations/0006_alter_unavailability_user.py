# Generated by Django 3.2.9 on 2022-03-06 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('availability', '0005_alter_unavailability_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unavailability',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
