from collections import Counter

from django.shortcuts import render
from django.http import HttpResponse


# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
#counter_show = Counter()
#counter_click = Counter()
landing_click = 0
alter_landing_click = 0
landing_counter_click = 0
alter_landing_counter_click = 0


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    global landing_counter_click, alter_landing_counter_click
    if request.GET.get == 'from-landing':
        landing_counter_click += 1
    else:
        alter_landing_counter_click += 1
    return render(request, "app/index.html")


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    choice = request.GET.get('ab-test-arg', 'original')
    global landing_click, alter_landing_click
    if choice == 'original':
        landing_click += 1
        return render(request, "app/landing.html")
    else:
        alter_landing_click += 1
        return render(request, "app/landing_alternate.html")


def stats(request):
    global landing_click, alter_landing_click,\
           landing_counter_click, alter_landing_counter_click
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:

    if landing_click and alter_landing_click:
        original_result = round(landing_counter_click / landing_click, 1)
        test_result = round(alter_landing_counter_click / alter_landing_click, 1)
        return render(request, "app/stats.html", context={
            'test_conversion': original_result,
            'original_conversion': test_result,
        })
    else:
        return HttpResponse('Try again!')
