from django import template

from application.models import ConstructionSite

register = template.Library()


@register.simple_tag(name='get_list_areas')
def get_constr_sites():
    return ConstructionSite.objects.all()


@register.inclusion_tag('application/list_areas.html')
def show_areas(arg1='Hello', arg2='world'):
    categories = ConstructionSite.objects.all()
    return {"categories": categories, "arg1": arg1, "arg2": arg2}