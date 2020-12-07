# Generated by Django 3.1.3 on 2020-12-06 03:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20201206_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='post_text',
        ),
        migrations.AddField(
            model_name='blog_post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
