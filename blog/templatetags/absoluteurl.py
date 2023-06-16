from django import template

register = template.Library()

@register.simple_tag(name='absoluteurl')
def absoluteurl(request, uri:str):
    try:
        absuri = request.build_absolute_uri(uri)
    except:
        absuri = request.build_absolute_uri()
    return {"uri": absuri }

