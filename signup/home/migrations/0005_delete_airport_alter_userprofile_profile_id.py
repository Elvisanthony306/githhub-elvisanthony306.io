# Generated by Django 5.1.4 on 2025-01-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_airport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Airport',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
