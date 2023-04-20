import os
import django
import csv
import sys
import math

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ksw_django_ptf.settings")

django.setup()

from dashboard.models import Opexseoul

CSV_PATH = './dashboard/datas/yangcheon/yangcheon.csv'

with open(CSV_PATH, 'r', encoding='utf-8') as file:
    data_rows = csv.reader(file, skipinitialspace=True)

    # print(data_rows)
    for row in data_rows:
        # print(row[2])
        row[2].isdigit()

        if row[2].isdigit():
            # print(row[2])
            row[2] = row[2]

            row[3] = row[3].replace(',','')

        # print(row[3].replace(',',''))

            Opexseoul.objects.create(
                regDate = row[0],
                restaurant = row[1],
                personnel = row[2],
                price = row[3],
                borough = 'yangcheon'
            )
