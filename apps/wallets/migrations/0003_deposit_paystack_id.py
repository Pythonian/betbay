# Generated by Django 5.1.1 on 2024-11-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_alter_deposit_options_wallet_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='paystack_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]