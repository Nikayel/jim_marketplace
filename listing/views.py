from django.shortcuts import render, get_object_or_404
# Create your views here.
from item.models import Item

def index(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request, 'listing/index.html',{
        'items': items,
    })

