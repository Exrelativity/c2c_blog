from django.shortcuts import redirect
import graphene

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed before the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed after the view is called, before the response is sent.

        return response


class AuthorizationMiddleware:
    def resolve(self, next, root, info, **args):
        user = info.context.user
        if not user.has_perm('post.can_publish_article'):
            raise Exception("Permission denied")
        return next(root, info, **args)


class AuthenticationMiddleware:
    def resolve(self, next, root, info, **args):
        user = info.context.user  # Assuming you have set the user in the context
        if not user.is_authenticated:
            raise Exception("Authentication required")
        return next(root, info, **args)
