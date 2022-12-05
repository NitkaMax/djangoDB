import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
import datetime as DT


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                rel_date = DT.datetime.strptime(line[4], '%Y-%m-%d').date()
                print(rel_date)
                slug = line[1].lower().replace(' ', '-')
                print(slug)
                p = Phone(name=line[1], image=line[2], price=line[3], release_date=rel_date, lte_exists=line[5], slug=slug)
                p.save()