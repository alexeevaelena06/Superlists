from django.shortcuts import render, redirect
from lists.models import Item
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/единственный-в-своем-роде-список-в-мире/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def view_list(request):
    """представление списка"""
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
