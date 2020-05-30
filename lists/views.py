# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from lists.models import Item
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    """домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/единственный-в-своем-роде-список-в-мире/')
    return render(request, 'home.html')


def view_list(request):
    """новый список"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
