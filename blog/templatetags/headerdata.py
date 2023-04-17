from django import template
from post.models import *
from userprofile.models import *

register = template.Library()


@register.simple_tag(name='headerdata')
def headerdata(request):
    try:
        category = Category.objects.filter(status=True, front=True)
    except:
        pass
    try:
        subcategory = SubCategory.objects.filter(status=True, front=True)
    except:
        pass
    if request.user.id:
        try:
            profile = UsersProfile.objects.get(userId=request.user.id)
        except:
            profile = {}
            
    return {
        "category": category,
        "subcategory": subcategory,
        "profile": profile
        }

