# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from lists.models import Item, List
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    """домашняя страница"""
    return render(request, 'home.html')


def view_list(request, list_id):
    """представление списка"""
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items': items})


def new_list(request):
    """новый список"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/единственный-в-своем-роде-список-в-мире/')
