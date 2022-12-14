# Generated by Django 3.2.4 on 2022-07-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oais', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('can_view_system_settings', 'Can view System Settings')]},
        ),
        migrations.AddField(
            model_name='archive',
            name='invenio_parent_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='archive',
            name='invenio_parent_url',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='archive',
            name='invenio_version',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='step',
            name='name',
            field=models.IntegerField(choices=[(1, 'Sip Upload'), (2, 'Harvest'), (3, 'Validation'), (4, 'Checksum'), (5, 'Archive'), (6, 'Edit Manifest'), (7, 'Invenio Rdm Push')]),
        ),
    ]
