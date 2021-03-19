import datetime
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString

register = template.Library()


@register.filter(name="comma")
@stringfilter
def comma(value):
    return value.title()


@register.filter(is_safe=True)
def safe_string(value):
    return value


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
