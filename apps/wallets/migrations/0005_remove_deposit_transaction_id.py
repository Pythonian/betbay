# Generated by Django 5.1.1 on 2024-11-23 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0004_alter_deposit_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='transaction_id',
        ),
    ]