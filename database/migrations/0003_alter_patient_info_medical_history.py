# Generated by Django 4.2.5 on 2023-09-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_patient_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_info',
            name='medical_history',
            field=models.TextField(),
        ),
    ]
