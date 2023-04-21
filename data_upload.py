import os
import django
import csv
import sys
import math

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ksw_django_ptf.settings")

django.setup()

from dashboard.models import Opexseoul

CSV_PATH = './dashboard/datas/gwangjin/gwangjin.csv'

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

            if "스타벅스" not in row[1] and "투썸" not in row[1] and "할리스" not in row[1] and "폴바셋" not in row[1] and "정관장" not in row[1] and "파리크라상" not in row[1] and "마트" not in row[1] and "이디야" not in row[1] and "커피" not in row[1] and "맘스터치" not in row[1] and "카페" not in row[1] and "파리바" not in row[1] :
                

        # print(row[3].replace(',',''))

                Opexseoul.objects.create(
                    regDate = row[0],
                    restaurant = row[1],
                    personnel = row[2],
                    price = row[3],
                    borough = 'gwangjin'
                )
