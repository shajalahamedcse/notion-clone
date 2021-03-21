# Generated by Django 3.1 on 2021-01-31 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0027_pagelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelink',
            name='page_element',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='PageLink', to='chat_app.page_element'),
            preserve_default=False,
        ),
    ]