from django.urls import path
import apps.api.views as views
from rest_framework import routers

urlpatterns = [
    path("demo-function", views.my_view),
    path("demo-class", views.MyView.as_view()),
    path("products", views.ListProducts.as_view(), name="list_products"),
    path("products/generic", views.GenericListProducts.as_view(), name="generic_list_products"),
    path("products/create", views.create_product, name="create_product"),
]


router = routers.SimpleRouter()
router.register('products-router', views.ProductViewset)
urlpatterns = router.urls + urlpatterns
