# Generated by Django 3.1 on 2021-02-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0041_table_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_data',
            name='order',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]