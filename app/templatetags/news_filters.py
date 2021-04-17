from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    delta_sec = (datetime.now() - datetime.fromtimestamp(int(value))).total_seconds() #секунды
    delta = {
        'seconds' : int(delta_sec),
        'minutes' : int(delta_sec // 60),
        'hours' : int(delta_sec // 3600),
        'days' : int(delta_sec // 86400),
    }
        
    if delta['days'] >= 1:
       return datetime.fromtimestamp(value)
    else:
        if delta['minutes'] <= 10:
            return 'только что'
        elif delta['minutes'] < 60:
            return f"{delta['minutes']} минут назад"

        return f"{delta['hours']} часов назад"


@register.filter
def format_num_comments(value):
    value = int(value)
    if value < 0:
        return "Оставьте комментарий"
    elif 0 < value <= 50:
        return value
    else:
        return "50+"


@register.filter
def format_score(value, default=None):
    if value:
        value = int(value)
        if value < -5:
            return "все плохо"
        elif -5 <= value <= 5:
            return "нейтрально"
        else:
            return "все хорошо"
    else:
        return default

@register.filter
def format_selftext(value, count=None):
    value = value.split()
    count = int(count)
    first_count = ' '.join(value[0:count])
    last_count = ' '.join(value[len(value) - count::])

    print("first_count",first_count)
    print("last_count",last_count)


    return f'{first_count} ... {last_count}'

