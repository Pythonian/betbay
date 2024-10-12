# Generated by Django 5.1.1 on 2024-10-06 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_bundle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='group',
            field=models.OneToOneField(help_text='Select the group this bundle is associated with.', on_delete=django.db.models.deletion.CASCADE, related_name='bundle', to='accounts.group', verbose_name='Group'),
        ),
    ]