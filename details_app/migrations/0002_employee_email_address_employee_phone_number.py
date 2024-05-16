# Generated by Django 5.0.6 on 2024-05-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email_address',
            field=models.EmailField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
