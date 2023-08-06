from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm
from .models import Item
# Create your views here.


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    r_items = Item.objects.filter(catagory=item.catagory, is_sold=False).exclude(pk=pk)

    return render(request, 'item/detail.html', {
        'item': item,
        'r_items': r_items
    })

def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
         form = NewItemForm()
    return render(request, 'item/form.html', {'form': form, 'title': 'New item'})