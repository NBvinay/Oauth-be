from django.http import HttpResponse
from rest_framework.views import APIView


class DemoApi(APIView):
    def get(self, *args, **kwargs):

        return HttpResponse(status=200, content="This is the response of demo API")
