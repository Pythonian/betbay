# Generated by Django 5.1.1 on 2024-12-05 18:50

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(help_text='Enter a unique name for the betting group.', max_length=255, unique=True, verbose_name='Group Name')),
                ('description', models.TextField(help_text='Provide a detailed description of the betting group.', max_length=140, verbose_name='Description')),
                ('status', models.CharField(choices=[('R', 'Running'), ('C', 'Closed')], db_index=True, default='R', help_text='Select a status for the betting group.', max_length=1, verbose_name='Status')),
                ('bettors', models.ManyToManyField(blank=True, help_text='Users who are part of this group.', related_name='bet_groups', to=settings.AUTH_USER_MODEL, verbose_name='Bettors')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bundle_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(help_text='Enter a unique name for the group bundle.', max_length=255, unique=True, verbose_name='Bundle Name')),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter the price for one bundle.', max_digits=10, verbose_name='Bundle Price')),
                ('winning_percentage', models.DecimalField(decimal_places=2, help_text='Enter the percentage of the bundle price that will be returned as winnings. E.g., 20 for 20%.', max_digits=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Winning Percentage')),
                ('min_bundles_per_user', models.PositiveIntegerField(help_text='Minimum number of bundles a user can purchase.', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Minimum Bundles per User')),
                ('max_bundles_per_user', models.PositiveIntegerField(help_text='Maximum number of bundles a user can purchase.', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Maximum Bundles per User')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('W', 'Won'), ('L', 'Lost')], default='P', help_text='Current status of the bundle.', max_length=1, verbose_name='Status')),
                ('participants', models.ManyToManyField(blank=True, help_text='Users who have purchased this bundle.', related_name='bundles', to=settings.AUTH_USER_MODEL, verbose_name='Participants')),
                ('group', models.OneToOneField(help_text='Select the group this bundle is associated with.', on_delete=django.db.models.deletion.CASCADE, related_name='bundle', to='groups.group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Bundle',
                'verbose_name_plural': 'Bundles',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('purchase_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('payout_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Payout Amount')),
                ('reference', models.CharField(help_text='Unique ID of the bundle purchase transaction', max_length=20, unique=True, verbose_name='Reference')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('C', 'Cancelled')], default='P', max_length=1, verbose_name='Status')),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='groups.bundle', verbose_name='Bundle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['status'], name='groups_grou_status_952d41_idx'),
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['name'], name='groups_grou_name_0806de_idx'),
        ),
    ]