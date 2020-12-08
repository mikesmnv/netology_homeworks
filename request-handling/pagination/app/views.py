from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv


def index(request):
    return redirect(reverse(bus_stations))


bus_stations_list = []

with open(settings.BUS_STATION_CSV) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        bus_stations_list.append(row)


def bus_stations(request):
    paginator = Paginator(bus_stations_list, settings.ITEMS_PER_PAGE)
    current_page = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(current_page)
    if page_obj.has_next():
        next_page_url = reverse('bus_stations') + f'?page={page_obj.next_page_number()}'
    else:
        next_page_url = None
    if current_page > 1:
        prev_page_url = reverse('bus_stations') + f'?page={page_obj.previous_page_number()}'
    else:
        prev_page_url = None
    return render(request, 'index.html', context={
        'bus_stations': page_obj,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
