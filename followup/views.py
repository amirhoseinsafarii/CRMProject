
import select
from django.db.models.base import Model
from django.views.generic import CreateView, DetailView, UpdateView, ListView
import selectors
from organization import models
from products import models

from django.utils.translation import LANGUAGE_SESSION_KEY, ugettext_lazy as _
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse, request, response
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateResponseMixin
from . import models, forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.management.base import BaseCommand
from django.urls import reverse_lazy
from . import models


class FollowUpCreate(LoginRequiredMixin,CreateView):
    model = models.FollowUP
    form_class = forms.FollwUpForm
    success_url = reverse_lazy('organization:list-organization')
    extra_context = {
        'page_title': 'create followup'
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ListFollowUp(ListView):

    queryset = models.FollowUP.objects.all()
