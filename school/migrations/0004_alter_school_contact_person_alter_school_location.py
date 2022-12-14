# Generated by Django 4.0 on 2022-10-24 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_school_contact_person_alter_school_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='contact_person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.contactperson'),
        ),
        migrations.AlterField(
            model_name='school',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.location'),
        ),
    ]
