

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, render
from . import models

from django.http import HttpResponse
from wsgiref.util import FileWrapper


class ListProduct(LoginRequiredMixin,ListView):
    """
        show list of products
    """
    queryset = models.Product.objects.all()

