# Generated by Django 3.1.6 on 2025-03-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectbatch',
            name='email',
            field=models.CharField(default=2, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selectbatch',
            name='studentname',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
