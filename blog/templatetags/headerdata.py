from django import template
from post.models import *
from userprofile.models import *

register = template.Library()


@register.filter(name='headerdata')
def headerdata(request):
    try:
        category = [x for x in Category.objects.filter(status=True, front=True)]
    except Category.DoesNotExist:
        pass
    try:
        subcategory = [x for x in SubCategory.objects.filter(status=True, front=True)]
    except SubCategory.DoesNotExist:
        pass
    try:
        profile = UsersProfile.objects.get(userId=request.user.id)
    except UsersProfile.DoesNotExist:
        pass
    return {
        "category": category,
        "subcategory": subcategory,
        "profile": profile
    }

