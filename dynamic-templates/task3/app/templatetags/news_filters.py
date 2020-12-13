from django import template
import datetime

register = template.Library()


@register.filter
def format_date(value):
    new_value = datetime.datetime.fromtimestamp(value)
    delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(value)
    if delta.seconds <= 600:
        return 'только что'
    elif (delta.seconds // 3600) <= 24:
        return '{0} часов назад'.format(delta.seconds // 3600)
        #return new_value.date()
    else:
        return new_value.date()


@register.filter
def format_score(value):
    if value < -5:
        return 'все плохо'
    elif value > 5:
        return 'хорошо'
    else:
        return 'нейтрально'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif value > 50:
        return '50+'
    else:
        return value
