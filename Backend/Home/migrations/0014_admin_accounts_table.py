# Generated by Django 3.2.21 on 2023-12-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_admin_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_accounts_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('rollNumber', models.CharField(max_length=255)),
            ],
        ),
    ]
