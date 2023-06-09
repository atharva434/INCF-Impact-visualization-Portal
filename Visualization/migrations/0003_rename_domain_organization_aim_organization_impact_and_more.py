# Generated by Django 4.1.6 on 2023-07-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Visualization", "0002_organization_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="organization",
            old_name="domain",
            new_name="aim",
        ),
        migrations.AddField(
            model_name="organization",
            name="impact",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="use",
            field=models.TextField(blank=True, null=True),
        ),
    ]
