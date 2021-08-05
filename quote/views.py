import weasyprint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms

class QuoteList(LoginRequiredMixin, ListView):
    
    model = models.Quote
    template_name = "quote/qupte_list.html"

class QuoteCreate(LoginRequiredMixin, CreateView):
    model = models.Quote
    form_class = forms.QuoteForm
    template_name = 'quote/quote_create.html'
    success_url = reverse_lazy('quote:quote-list')

    def form_valid(self, form):
        form.instance.user= self.request.user
        r = form.instance.user
        r.save()
        return super().form_valid(form)


class QuoteItemCreate(LoginRequiredMixin, CreateView):
    model = models.QuoteItem
    form_class = forms.QuoteItemForm
    template_name = 'quote/quoteitem_create.html'

    success_url = reverse_lazy('quote:quote-list')

class QuotePrint(LoginRequiredMixin, DetailView):
    model = models.Quote
    template_name = 'quote/quote_detail.html'

    def get(self, request, *args, **kwargs):
        p = super().get(request, *args, **kwargs)
        rendered_content = p.rendered_content
        pdf = weasyprint.HTML(string=rendered_content, base_url='http://127.0.0.1:8000/').write_pdf()
        response = HttpResponse(pdf, content_type='appLication/pdf')
        return response