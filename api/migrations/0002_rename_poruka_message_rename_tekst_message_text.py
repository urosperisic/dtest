# Generated by Django 5.2.3 on 2025-06-11 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Poruka',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='tekst',
            new_name='text',
        ),
    ]
