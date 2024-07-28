from django import template
register = template.Library()

CEN_LIST = [
    'Fuck',
    'fuck',
    'Shit',
    'shit',
]
@register.filter(name='censor')
def censor(value, arg):
    text = value
    cen = arg
    for word in CEN_LIST:
        if word.lower() in text.lower():
            text = text.replace(word, cen)
    return text