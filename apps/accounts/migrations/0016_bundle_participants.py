# Generated by Django 5.1.1 on 2024-10-20 13:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_deposit_paystack_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='participants',
            field=models.ManyToManyField(blank=True, help_text='Users who have purchased this bundle.', related_name='bundles', to=settings.AUTH_USER_MODEL, verbose_name='Participants'),
        ),
    ]
