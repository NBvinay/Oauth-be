from django.http import HttpResponse
from oauth2_provider.models import AccessToken, RefreshToken


def del_user(request):
    try:
        print("del headers", request.headers['Authorization'])
        accessToken = request.headers['Authorization'][7:]
        AccessToken.objects.get(token=accessToken).delete()

        return HttpResponse(status=200)
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
