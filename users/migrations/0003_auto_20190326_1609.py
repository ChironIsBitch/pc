# Generated by Django 2.1.5 on 2019-03-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190326_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
    ]
