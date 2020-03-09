from django.shortcuts import render, redirect
from lists.models import Item
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    return render(request, 'home.html')
