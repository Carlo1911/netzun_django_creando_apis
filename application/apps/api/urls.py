from django.urls import path
from .views import my_view, MyView

urlpatterns = [
    path("my-view/", my_view, name="my-view"),
    path("my-view-class/", MyView.as_view(), name="my-view-class"),
]
