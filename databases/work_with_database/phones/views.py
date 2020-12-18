from django.shortcuts import render
from phones.models import Phone

phones = None


def show_catalog(request):
    sort = request.GET.get("sort")
    if sort:
        global phones
        if sort == "name":
            phones = Phone.objects.order_by('name')
        else:
            phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(slug)
    phone = Phone.objects.filter(slug=slug)  # почему-то не работает
    context = {'phone': phone}
    return render(request, template, context)
