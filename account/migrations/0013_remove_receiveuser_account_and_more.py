# Generated by Django 5.0.1 on 2024-02-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_receiveuser_options_alter_senduser_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiveuser',
            name='account',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='identity_type',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='account',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='identity_type',
        ),
        migrations.AddField(
            model_name='senduser',
            name='mobile',
            field=models.CharField(default='000000000', max_length=15),
        ),
        migrations.AlterField(
            model_name='receiveuser',
            name='identity_image',
            field=models.ImageField(blank=True, null=True, upload_to='receiveuser'),
        ),
        migrations.AlterField(
            model_name='receiveuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='receiveuser'),
        ),
        migrations.AlterField(
            model_name='senduser',
            name='account_number',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='senduser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='senduser'),
        ),
    ]