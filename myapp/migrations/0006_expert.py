# Generated by Django 3.2 on 2021-05-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210518_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_email', models.EmailField(max_length=254)),
                ('FullName', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.TextField(blank=True, null=True)),
                ('jobTitle', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=30)),
                ('profile_pic', models.ImageField(blank=True, upload_to='data')),
            ],
        ),
    ]
