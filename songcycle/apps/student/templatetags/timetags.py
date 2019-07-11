from django import template
from pytz import timezone
import datetime
register = template.Library()

@register.filter(name="to_jst")
def to_jst(timestamp):
    return timestamp.astimezone(timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")
