# Generated by Django 5.1.1 on 2024-10-28 02:19

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_remove_deposit_reference_alter_deposit_paystack_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='payout_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Payout Amount'),
        ),
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, help_text='The amount the bettor will be paid.', max_digits=10, verbose_name='Amount')),
                ('note', models.TextField(blank=True, help_text='An optional note by the admin.', verbose_name='Payout Note')),
                ('transaction_id', models.CharField(blank=True, help_text='Transaction ID for the payout.', max_length=150, verbose_name='Paystack Transaction ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('F', 'Failed')], default='P', max_length=1, verbose_name='Status')),
                ('paid_on', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payouts', to='accounts.bundle', verbose_name='Bundle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payouts', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Payout',
                'verbose_name_plural': 'Payouts',
                'ordering': ['-created'],
            },
        ),
    ]