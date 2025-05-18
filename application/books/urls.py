from django.urls import path

from .views import books_view, BooksViewClass

urlpatterns = [
    path("view/", books_view, name="my-view"),
    path("view-class/", BooksViewClass.as_view(), name="my-view-class"),
]
