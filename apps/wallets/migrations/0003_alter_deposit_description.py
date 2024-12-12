# Generated by Django 5.1.1 on 2024-12-08 02:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_alter_withdrawal_options_alter_withdrawal_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='description',
            field=models.CharField(blank=True, default='', help_text='Description of the Wallet Deposit', max_length=50, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(50)], verbose_name='Description'),
        ),
    ]