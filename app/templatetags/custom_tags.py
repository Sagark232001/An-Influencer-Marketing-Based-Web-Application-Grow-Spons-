from django import template
import inflect

register = template.Library()

@register.filter(name='post_id_list')
def post_id_list(data):
    ls = [i.id for i in data]
    return ls

@register.filter(name='post_id_list1')
def post_id_list1(data):
    ls = [i.post.id for i in data]
    return ls

@register.filter(name='int_to_word')
def int_to_word(data):
    p = inflect.engine()
    num = p.number_to_words(data)
    return num
