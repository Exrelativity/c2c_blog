from django import template
from file.models import File

register = template.Library()


@register.simple_tag(name='files')
def files(request):
    if request.user.id:
        try:
            file = File.objects.get(userId=request.user.id)
        except:
            file = {}
            
    return {
        "file": file
        }

