# Generated by Django 2.1.5 on 2019-03-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20190329_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='start',
            name='t_file',
            field=models.FileField(blank=True, null=True, upload_to='file/%Y%m'),
        ),
    ]
