# Generated by Django 4.2.6 on 2023-10-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirQualityData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('aqi_bucket', models.CharField(max_length=20)),
                ('pm25', models.FloatField()),
                ('pm10', models.FloatField()),
                ('no', models.FloatField()),
                ('no2', models.FloatField()),
                ('nox', models.FloatField()),
                ('nh3', models.FloatField()),
                ('co', models.FloatField()),
                ('so2', models.FloatField()),
                ('o3', models.FloatField()),
                ('benzene', models.FloatField()),
                ('toluene', models.FloatField()),
                ('xylene', models.FloatField()),
            ],
        ),
    ]
