import csv
from pprint import pprint

def test_import():
    with open('phones.csv', 'r') as file:
        phones = list(csv.DictReader(file, delimiter=';'))

        pprint(phones)

test_import()