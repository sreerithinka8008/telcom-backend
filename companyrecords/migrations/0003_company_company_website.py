# Generated by Django 5.1.6 on 2025-02-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyrecords', '0002_company_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_website',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
