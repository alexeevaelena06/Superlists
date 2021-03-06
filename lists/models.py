from django.db import models


class List(models.Model):
    """новый список"""
    pass


class Item(models.Model):
    """элемент списка"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
