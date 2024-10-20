# Generated by Django 5.1.1 on 2024-10-12 11:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_ticket_created'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(blank=True, help_text='Tell us about yourself in 140 characters.', max_length=140, verbose_name='about')),
                ('email_confirmed', models.BooleanField(default=False, help_text="Determine if the User's email has been confirmed.", verbose_name='email confirmed?')),
                ('verified_account', models.BooleanField(default=False, verbose_name='verified account?')),
                ('location', models.CharField(blank=True, max_length=30, null=True, verbose_name='location')),
                ('is_banned', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
