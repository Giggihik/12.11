from django.shortcuts import render, HttpResponse
from .models import Item, Manufacturer

from django.db.models import Sum, Avg, F, Min

def get_items(request):
    items = (
        Item
        .objects
        .filter(manufacturer__name= 'Рога и Копыта')
        .aggregate(
            price_sum_min=Min(F('price') * F('quantity')), 
        )
    )
    min_sum = items['price_sum_min']
    
    context = {
        'min_sum': min_sum 
        }
            
    return render(request, "items-catalog.html", context)