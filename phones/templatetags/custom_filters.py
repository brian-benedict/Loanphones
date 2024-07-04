# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='get_icon_class')
def get_icon_class(title):
    if title == 'Efficient':
        return 'fa-bolt'
    elif title == 'Convenient':
        return 'fa-calendar-alt'
    elif title == 'Transparent':
        return 'fa-handshake'
    else:
        return 'fa-question-circle'


@register.filter
def remove_decimals(value):
    return int(value)