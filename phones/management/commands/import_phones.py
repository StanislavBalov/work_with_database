import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.conf import settings

class Command(BaseCommand):
    help = 'Import phones from a CSV file'
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                phone = Phone(
                    id=line['id'],
                    name=line['name'],
                    price=line['price'],
                    image=line['image'],
                    release_date=line['release_date'],
                    lte_exists=line['lte_exists'].lower() == 'true'
                )
                phone.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))
        pass
