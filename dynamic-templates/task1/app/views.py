import csv
import os
from django.shortcuts import render
from django.conf import settings

inflation_list = []
with open(os.path.join(settings.BASE_DIR, 'inflation_russia.csv'), encoding='utf-8') as csv_file:
    headers = list(next(csv.reader(csv_file, delimiter=';')))
with open(os.path.join(settings.BASE_DIR, 'inflation_russia.csv'), encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        inflation_list.append(row)


def inflation_view(request):
    template_name = 'app/inflation.html'
    context = {'inflation_list': inflation_list,
               'headers': headers}
    return render(request, template_name,
                  context)
