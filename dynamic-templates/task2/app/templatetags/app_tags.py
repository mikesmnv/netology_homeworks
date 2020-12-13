from django import template


register = template.Library()


@register.simple_tag()
def is_active(value_1, value_2):
    if value_1 == value_2:
        return "active"
    else:
        return None
