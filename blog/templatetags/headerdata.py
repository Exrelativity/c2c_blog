from django import template
from post.models import *
from userprofile.models import *

register = template.Library()


@register.filter(name='headerdata')
def headerdata(request):
    category = [x for x in Category.objects.filter(status=True, front=True)]
    subcategory = [x for x in SubCategory.objects.filter(status=True, front=True)]
    profile = UsersProfile.objects.get(userId=request.user.id)
    return {
        "category": category,
        "subcategory": subcategory,
        "profile": profile
    }

