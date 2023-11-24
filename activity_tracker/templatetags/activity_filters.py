from django import template

register = template.Library()

@register.filter
def pluck(items, attr):
    return [getattr(item, attr, None) for item in items]
