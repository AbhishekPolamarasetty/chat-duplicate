# Generated by Django 3.2.15 on 2024-01-24 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_postmodel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='username',
        ),
    ]
