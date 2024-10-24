# Generated by Django 5.1.1 on 2024-10-13 02:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_deposit'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity'),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=255, verbose_name='verb')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('target_id', models.PositiveIntegerField(blank=True, null=True)),
                ('target_ct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_obj', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='accounts_ac_created_ecacea_idx'), models.Index(fields=['target_ct', 'target_id'], name='accounts_ac_target__d7e79e_idx')],
            },
        ),
    ]
