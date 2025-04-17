from django.http import JsonResponse
from django.views import View


def my_view(request):
    if request.method == "GET":
        return JsonResponse({"success": True})


class MyView(View):
    def get(self, request):
        return JsonResponse({"success": True})
