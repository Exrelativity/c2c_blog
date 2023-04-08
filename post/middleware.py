from .models import *
from django.shortcuts import redirect


def category_provider_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not (
            request.session.__contains__("category")
            or request.session.__contains__("subCategory")
        ):
            try:
                category = Category.objects.get(status=True)[:5]
                subCategory = SubCategory.objects.get(status=True)
                request.session.__setitem__("category", category)
                request.session.__setitem__("subCategory", subCategory)
            except Category.DoesNotExist:
                pass

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if not (
            request.session.__contains__("category")
            or request.session.__contains__("subCategory")
        ):
            try:
                category = Category.objects.get(status=True).exists()[:5]
                subCategory = SubCategory.objects.get(status=True).exists()
                request.session.__setitem__("category", category)
                request.session.__setitem__("subCategory", subCategory)
            except Category.DoesNotExist:
                pass

        return response

    return middleware
