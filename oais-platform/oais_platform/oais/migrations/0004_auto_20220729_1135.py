# Generated by Django 3.2.4 on 2022-07-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oais', '0003_auto_20220728_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadjob',
            name='sip_dir',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='uploadjob',
            name='tmp_dir',
            field=models.CharField(max_length=1000),
        ),
    ]