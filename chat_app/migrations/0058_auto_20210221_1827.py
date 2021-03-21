# Generated by Django 3.1 on 2021-02-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0057_page_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='page_element',
            name='column',
            field=models.CharField(default='A', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page_element',
            name='group',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]