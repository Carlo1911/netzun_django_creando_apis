from django.http import JsonResponse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.api.models import Product
from apps.api.serializers import CompleteProductSerializer, ProductSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return JsonResponse({'result': 'success', 'data': {}})


class MyView(View):
    def get(self, request):
        # <view logic>
        return JsonResponse({'result': 'success', 'data': {}})


@api_view(['POST'])
def create_product(request):
    serializer = CompleteProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class ListProducts(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all products.
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class GenericListProducts(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class ProductViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination

    @method_decorator(cache_page(60*2))  # 2 minutes
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)













# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class ExampleView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)
