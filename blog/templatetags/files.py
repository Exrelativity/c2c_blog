from django import template
from file.models import File

register = template.Library()


@register.simple_tag(name='headerdata')
def files(request):
    if request.user.id:
        try:
            profile = File.objects.get(userId=request.user.id)
        except:
            profile = {}
            
    return {
        "category": category,
        "subcategory": subcategory,
        "profile": profile
        }

