from oauth2_provider.models import  AccessToken
from django.http import JsonResponse


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("initialized middleware")

    def __call__(self, request):
        response = self.get_response(request)
        try:
            if request.path in ['/auth/token/', '/auth/convert-token/']:
                res = {'access_token': response.data['access_token'],
                       'expires_in': response.data['expires_in'],
                       'refresh_token': response.data['refresh_token'],
                       'user_name': AccessToken.objects.filter(token=response.data['access_token'])[0].user.__str__()}
                return JsonResponse(res)
        except Exception as e:
            print(e)
        return response
