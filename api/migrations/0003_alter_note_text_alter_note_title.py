# Generated by Django 4.1.9 on 2023-05-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_note_text_alter_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
