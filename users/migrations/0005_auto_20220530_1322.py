# Generated by Django 3.2.8 on 2022-05-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_account_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='age',
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
