# Generated by Django 3.2 on 2021-05-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='city',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
