from django import template


register = template.Library()


@register.filter(name='modelus')
def modelus(value, x):
    try:
        return value % x
    except AttributeError:
        return ""

