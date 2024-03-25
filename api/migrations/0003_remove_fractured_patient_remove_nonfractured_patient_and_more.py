# Generated by Django 5.0.3 on 2024-03-23 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_patient_description_fractured_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fractured',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='nonfractured',
            name='patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='fractured_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fractured_patients', to='api.fractured'),
        ),
        migrations.AddField(
            model_name='patient',
            name='non_fractured_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='non_fractured_patients', to='api.nonfractured'),
        ),
    ]