# Generated by Django 3.2.3 on 2021-06-27 16:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_art_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
