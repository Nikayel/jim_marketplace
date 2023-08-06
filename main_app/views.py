from django.shortcuts import render, redirect
from item.models import Catagory, Item
# Create your views here.
from .forms import SignUpForm
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    catagories = Catagory.objects.all()
    return render(request, 'main_app/index.html',{
        'items': items,
        'catagories': catagories
    })

def contact(request):
    return render(request, 'main_app/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/login/')
    else:
        form = SignUpForm()
    return render(request, 'main_app/signup.html', {'form': form})