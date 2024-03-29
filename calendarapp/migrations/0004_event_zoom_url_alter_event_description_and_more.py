# Generated by Django 5.0.2 on 2024-02-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_alter_event_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='zoom_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=20000),
        ),
    ]
