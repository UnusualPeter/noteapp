# Generated by Django 3.0.5 on 2020-04-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_note', models.CharField(max_length=100)),
                ('content_note', models.TextField()),
                ('created_note', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Notes',
            },
        ),
    ]