# Generated by Django 4.0.4 on 2022-06-01 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_is_delete_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_delete',
            new_name='is_deleted',
        ),
    ]