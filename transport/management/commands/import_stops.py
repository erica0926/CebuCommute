import csv
from django.core.management.base import BaseCommand
from transport.models import Stop


class Command(BaseCommand):
    help = 'Import stops from CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'stops.csv'

        with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                stop_id = row['stop_id']
                stop_name = row['stop_name']

                # Avoid duplicates
                stop, created = Stop.objects.get_or_create(
                    stop_id=stop_id,
                    defaults={'stop_name': stop_name}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added: {stop_name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Already exists: {stop_name}'))
