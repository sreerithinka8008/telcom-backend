# Generated by Django 5.1.6 on 2025-02-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyrecords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
