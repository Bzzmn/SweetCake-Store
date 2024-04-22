from django import template

register = template.Library()

@register.filter(name='intdot')
def intdot(value):
    # """Convert an integer to a string with dots as thousands separators."""
    original_format = f"{value:,}"
    return original_format.replace(',', '.')