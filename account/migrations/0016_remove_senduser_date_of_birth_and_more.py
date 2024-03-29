# Generated by Django 5.0.1 on 2024-02-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_senduser_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senduser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='identity_image',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='identity_type',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='signature',
        ),
        migrations.AddField(
            model_name='senduser',
            name='full_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='senduser',
            name='other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
