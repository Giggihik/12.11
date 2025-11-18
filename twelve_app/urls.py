from django.urls import path
from .views import get_total_book_count #, display_item

urlpatterns = [
    path('', get_total_book_count)
]