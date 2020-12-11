from django import template
from app import views

register = template.Library()


@register.simple_tag()
def get_color(curr_list, head):
    value = views.inflation_list[views.inflation_list.index(curr_list)][head]
    if value != '':
        value = float(value)
        if value < 0:
            return 'GreenYellow'
        elif 1 <= value <= 2:
            return 'LightCoral'
        elif 2 < value <= 5:
            return 'IndianRed'
        elif value > 5:
            return 'Crimson'
    else:
        pass


@register.simple_tag()
def get_value(curr_list, head):
    value = views.inflation_list[views.inflation_list.index(curr_list)][head]
    if value != '':
        return value
    else:
        return '-'


@register.simple_tag()
def get_color_grey():
    return 'LightGrey'
