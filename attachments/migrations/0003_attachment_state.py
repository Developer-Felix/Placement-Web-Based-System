# Generated by Django 3.2.8 on 2022-06-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0002_attachment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='state',
            field=models.CharField(choices=[(1, True), (0, False)], default=0, max_length=25),
        ),
    ]
