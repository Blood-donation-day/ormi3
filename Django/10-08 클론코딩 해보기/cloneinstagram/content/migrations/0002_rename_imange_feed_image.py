# Generated by Django 4.2.6 on 2023-10-09 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='imange',
            new_name='image',
        ),
    ]
