import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            name = phone['name']
            price = phone['price']
            image = phone['image']
            release_date = phone['release_date']
            lte_exist = phone['lte_exists']
            slug = slugify(name)
            phone_model = Phone(name=name,
                                price=price,
                                image=image,
                                release_date=release_date,
                                lte_exist=lte_exist,
                                slug=slug)
            phone_model.save()



