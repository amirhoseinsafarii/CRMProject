from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse, request, response
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from products import models
from . import models
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.exceptions import NotAuthenticated
from . import models, serializers, permissions


class ListOrganization(LoginRequiredMixin,ListView):
    """
    list of organizations
    """
    queryset = models.Organization.objects.all()
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ListOrganization, self).get_context_data(**kwargs) 
        list_exam = models.Organization.objects.all()
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
            
        context['list_exams'] = file_exams
        return context
        
class ViewOrganization(LoginRequiredMixin,DetailView):
    """
        detail of organization
    """
    model = models.Organization
   

class CreateOrganization(LoginRequiredMixin, CreateView):
    """
        create a organization
    """
    model = models.Organization
    form_class = forms.OrganizationForm
    success_url = reverse_lazy('organization:list-organization')
    extra_context = {
        'page_title': 'Create a organization'
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditOrganization(LoginRequiredMixin ,UpdateView):
    """
        edit a organization
    """
    model = models.Organization
    form_class = forms.OrganizationForm
    template_name = 'organization/edit_organization.html'
    success_url = reverse_lazy('organization:list-organization')

def Home_page(request):
    return render(request, 'organization/home_page.html')
"""
DRF Views
"""
class OrganizationViewSet(viewsets.ModelViewSet):
    
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [permissions.Iscreator]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_anonymous:
            raise NotAuthenticated('You need to be logged on.')
        user = self.request.user
        return qs.filter(user=user)




