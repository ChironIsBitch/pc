# Generated by Django 2.1.5 on 2019-03-30 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile_t_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='t_file',
        ),
    ]
