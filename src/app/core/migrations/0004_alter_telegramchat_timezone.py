# Generated by Django 5.0.6 on 2024-05-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_telegramchat_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramchat',
            name='timezone',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
