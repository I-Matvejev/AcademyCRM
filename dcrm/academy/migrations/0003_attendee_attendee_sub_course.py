# Generated by Django 5.0.2 on 2024-05-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_remove_attendee_attendee_contact_fathers_name_rus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='attendee_sub_course',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
