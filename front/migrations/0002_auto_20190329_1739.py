# Generated by Django 2.1.5 on 2019-03-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='start',
            name='beizhu',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='start',
            name='end_choices',
            field=models.CharField(choices=[('ys', '阳山'), ('qy', '清远'), ('gz', '广州')], default='ys', max_length=20, verbose_name='到达地点'),
        ),
        migrations.AlterField(
            model_name='start',
            name='name',
            field=models.CharField(blank=True, max_length=20, verbose_name='车型+可载人数'),
        ),
        migrations.AlterField(
            model_name='start',
            name='start_choices',
            field=models.CharField(choices=[('ys', '阳山'), ('qy', '清远'), ('gz', '广州')], default='ys', max_length=20, verbose_name='出发地点'),
        ),
    ]