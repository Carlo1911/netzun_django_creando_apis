from django.http import JsonResponse
from django.views import View


def books_view(request):
    if request.method == "GET":
        return JsonResponse({"success": True})


class BooksViewClass(View):
    def get(self, request):
        return JsonResponse({"success": True})
