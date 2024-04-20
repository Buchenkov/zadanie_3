from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.now().strftime(format_string)


# тег, который будет брать текущие параметры запроса и по
# указанному аргументу производить замену, не очищая остальные параметры.
@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()
