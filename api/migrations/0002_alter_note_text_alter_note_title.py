# Generated by Django 4.1.9 on 2023-05-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
