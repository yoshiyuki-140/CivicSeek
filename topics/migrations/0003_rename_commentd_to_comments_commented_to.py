# Generated by Django 4.2.5 on 2023-10-15 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_rename_topic_comments_commentd_to_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='commentd_to',
            new_name='commented_to',
        ),
    ]