# Generated by Django 3.2 on 2021-05-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_contactus_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
