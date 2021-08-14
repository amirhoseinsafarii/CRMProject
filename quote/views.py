from django.urls.base import is_valid_path
import weasyprint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from organization.models import Organization


class QuoteList(LoginRequiredMixin, ListView):
    """
        show list of quote
    """

    model = models.Quote
    template_name = "quote/qupte_list.html"

class QuoteCreate(LoginRequiredMixin, CreateView):
    """
        create a quote for an organization
    """

    model = models.Quote
    form_class = forms.QuoteForm
    template_name = 'quote/quote_create.html'
    success_url = reverse_lazy('quote:quote-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk', None)
        return context

    def form_valid(self, form):
        form.instance.user= self.request.user
        form.instance.organization = Organization.objects.get(pk=self.get_context_data().get('pk'))
        form.save()
        return super().form_valid(form)


class QuoteItemCreate(LoginRequiredMixin, CreateView):
    """
        create qouetitem for organizations (class)
    """

    model = models.QuoteItem
    form_class = forms.QuoteItemForm
    template_name = 'quote/quoteitem_create.html'

    success_url = reverse_lazy('quote:quote-list')

        
@login_required
def create_quoteitem(request, pk):
    """
        create qouetitem for organizations
    """

    form_instance = forms.QuoteItemForm()

    if request.method == 'POST':
        form_instance = forms.QuoteItemForm(data=request.POST, files=request.FILES)
        if form_instance.is_valid():
            form_instance.instance.user = request.user
            post_instance = get_object_or_404(klass=models.Quote, pk=pk)
            form_instance.instance.quote = post_instance
            form_instance.save()
            return redirect('quote:quote-list')

    return render(request, 'quote/quoteitem_create.html', {
        'form': form_instance,
        'page_title': 'create a new post',
    })

class QuotePrint(LoginRequiredMixin, DetailView):
    """
        print pdf of quote
    """
    model = models.Quote
    template_name = 'quote/quote_detail.html'

    def get(self, request, *args, **kwargs):
        p = super().get(request, *args, **kwargs)
        rendered_content = p.rendered_content
        pdf = weasyprint.HTML(string=rendered_content, base_url='http://127.0.0.1:8000/').write_pdf()
        response = HttpResponse(pdf, content_type='appLication/pdf')
        return response