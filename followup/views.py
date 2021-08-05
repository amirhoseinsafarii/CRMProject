
from django.template.loader import render_to_string
from followup.tasks import send_email_task
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from organization import models
from products import models
from quote.models import Quote
from django.http import JsonResponse, request, response
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect, HttpResponse, redirect
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models
from django.contrib import messages


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
    
class FollowUpList(ListView):

    queryset = models.FollowUP.objects.all()


def email(request, pk):
    quote_instance = get_object_or_404(klass=Quote, pk=pk)
    sender = request.user.username
    body = render_to_string(template_name='quote/quote_detail.html', context={'object': quote_instance})
    receiver = quote_instance.organization.email
    send_email_task(body, receiver, sender)
    messages.success(request, 'email sent successfuly')
    return redirect(reverse_lazy('quote:quote-list'))