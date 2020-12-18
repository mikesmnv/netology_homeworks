from django import template

register = template.Library()


@register.filter()
def text(value):
    if value:
        return "Да"
    else:
        return "Нет"
