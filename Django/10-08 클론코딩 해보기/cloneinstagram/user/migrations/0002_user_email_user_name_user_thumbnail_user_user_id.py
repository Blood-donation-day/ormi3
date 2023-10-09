# Generated by Django 4.2.6 on 2023-10-09 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='thumbnail',
            field=models.CharField(blank=True, default='default_profile.jpg', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
