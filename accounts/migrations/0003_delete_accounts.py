# Generated by Django 4.2.5 on 2023-10-06 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_accounts_birth_date_remove_accounts_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]