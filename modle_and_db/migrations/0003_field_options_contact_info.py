# Generated by Django 2.2 on 2019-12-24 08:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import modle_and_db.models


class Migration(migrations.Migration):

    dependencies = [
        ('modle_and_db', '0002_field_options_field_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='field_options',
            name='contact_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=modle_and_db.models.Field_Options.contact_default, verbose_name='ContactInfo'),
        ),
    ]
