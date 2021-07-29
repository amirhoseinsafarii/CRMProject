

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, render
from . import models



class ListProduct(LoginRequiredMixin,ListView):
    """
    list of products
    """
    queryset = models.Product.objects.all()

