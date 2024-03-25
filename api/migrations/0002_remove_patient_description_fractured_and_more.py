# Generated by Django 5.0.3 on 2024-03-23 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='description_fractured',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='description_not_fractured',
        ),
        migrations.AlterField(
            model_name='patient',
            name='Xray',
            field=models.FileField(null=True, upload_to='Xray/', verbose_name='Xray Image'),
        ),
        migrations.CreateModel(
            name='Fractured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_fractured', models.CharField(blank=True, help_text='Enter the description if the result is Fractured', max_length=1000, null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fractured_info', to='api.patient')),
            ],
        ),
        migrations.CreateModel(
            name='NonFractured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_not_fractured', models.CharField(blank=True, help_text='Enter the description if the result is Not Fractured', max_length=1000, null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='non_fractured_info', to='api.patient')),
            ],
        ),
    ]
