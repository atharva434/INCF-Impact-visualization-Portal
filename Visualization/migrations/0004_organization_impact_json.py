# Generated by Django 4.1.6 on 2023-08-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Visualization",
            "0003_rename_domain_organization_aim_organization_impact_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="impact_json",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
