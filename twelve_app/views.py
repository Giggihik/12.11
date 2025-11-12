from django.shortcuts import render
from .models import Item, Manufacturer

from django.db.models import Sum

def get_items(request):
    items = (
        Item
        .objects
        .all()
    )


    context = {
        'items': items
    }
    
    return render(request, 'items-catalog.html', context)