import csv
from django.core.management.base import BaseCommand
from setup.models import AirQualityData

class Command(BaseCommand):
    help = 'Load air quality data from CSV file'

    def handle(self, *args, **kwargs):
        csv_file = 'D:\Internship Luminar\Air Quality\city_day.csv'  # Specify the path to your CSV file

        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                AirQualityData.objects.create(
                    city=row['City'],
                    pm25=row['PM2.5'],
                    pm10=row['PM10'],
                    no=row['NO'],
                    no2=row['NO2'],
                    nox=row['NOx'],
                    nh3=row['NH3'],
                    co=row['CO'],
                    so2=row['SO2'],
                    o3=row['O3'],
                    benzene=row['Benzene'],
                    toluene=row['Toluene'],
                    xylene=row['Xylene'],
                    aqi=row['AQI'],
                    aqi_bucket=row['AQI_Bucket']
                )

        self.stdout.write(self.style.SUCCESS('Air quality data loaded successfully'))
