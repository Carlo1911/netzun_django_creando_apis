import json

import pytest
from django.http import JsonResponse
from django.test import RequestFactory

from books.views import books_view, BooksViewClass


@pytest.fixture
def factory():
    return RequestFactory()


def test_books_view_get(factory):
    # Arrange
    request = factory.get("/books/")

    # Act
    response = books_view(request)

    # Assert
    assert isinstance(response, JsonResponse)
    assert response.status_code == 200
    assert json.loads(response.content) == {"success": True}


def test_books_view_class_get(factory):
    # Arrange
    request = factory.get("/books/")
    view = BooksViewClass.as_view()

    # Act
    response = view(request)

    # Assert
    assert isinstance(response, JsonResponse)
    assert response.status_code == 200
    assert json.loads(response.content) == {"success": True}
