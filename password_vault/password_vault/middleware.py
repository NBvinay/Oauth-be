from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from google.oauth2 import id_token
from google.auth.transport import requests


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("initialized middleware")
        # One-time configuration and initialization.

    def __call__(self, request):

        if str(request.user) == 'AnonymousUser':
            print("No user detected")
            # return HttpResponse(status=500, content="No user detected")
            
        print("Request for user:", request.user, type(request.user), request.user.is_authenticated)
        response = self.get_response(request)
        print("response", response.status_code)

        return response
