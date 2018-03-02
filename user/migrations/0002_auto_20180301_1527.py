# Generated by Django 2.0.2 on 2018-03-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='所在城市'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('ONLINE', '在线'), ('OFFLINE', '离线')], default='OFFLINE', max_length=6, verbose_name='在线状态'),
        ),
    ]
