# Generated by Django 5.1.1 on 2024-11-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_profile_account_activated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='target_id',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]