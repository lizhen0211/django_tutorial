# Generated by Django 2.2 on 2019-12-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modle_and_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field_options',
            name='field_4',
            field=models.CharField(db_index=True, default='', max_length=32),
        ),
    ]
