# Generated by Django 4.0 on 2022-12-25 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school_description', models.TextField()),
                ('is_activated', models.BooleanField(default=False)),
                ('contact_person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.contactperson')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.location')),
            ],
        ),
    ]