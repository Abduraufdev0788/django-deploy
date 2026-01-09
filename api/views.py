from django.http import HttpRequest, HttpResponse
from django.views import View

class Testapi(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return HttpResponse("salom dunyo")