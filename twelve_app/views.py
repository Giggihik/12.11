from django.shortcuts import render, HttpResponse
from .models import Item, Manufacturer, Author, Publisher, Book

from django.db.models import Sum, Avg, F, Min, Count 

def get_total_book_count(request):
    
    total_books_data = Publisher.objects.annotate(
        book_count=Count('book')
    ).aggregate(
        total_p=Sum('book_count')
    )

   
    context = {
        'p': total_books_data['total_p'] or 0, 
    }
            

    return render(request, "print_agg_result.html", context)

