# Generated by Django 2.1.5 on 2019-03-30 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_start_t_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='start',
            name='t_file',
        ),
    ]
