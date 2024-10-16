# Generated by Django 3.2.3 on 2024-07-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visualization', '0007_fproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('senior', models.TextField(blank=True, null=True)),
                ('junior', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
