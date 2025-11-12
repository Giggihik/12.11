from django.urls import path
from .views import get_items #, display_item

urlpatterns = [
    path('', get_items)
]