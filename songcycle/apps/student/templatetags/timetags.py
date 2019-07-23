from django import template
from pytz import timezone

register = template.Library()


@register.filter(name="to_jst")
def to_jst(timestamp):
    if(timestamp is None):
        return ''
    return timestamp.astimezone(
        timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")
