# Generated by Django 3.0.5 on 2020-04-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='created_note',
            field=models.DateTimeField(auto_now_add=True, help_text='Date published'),
        ),
    ]