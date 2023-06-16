
from django.shortcuts import redirect



def current_user_middleware(get_response):
    # One-time configuration and initialization.
    
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
       
    

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.


        return response

    return middleware


class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        # if info.field_name == 'user':
        #     return None
        return next(root, info, **args)
    
class AuthenticationMiddleware(object):
    def resolve(self, next, root, info, **args):
        # if info.field_name == 'user':
        #     return None
        return next(root, info, **args)