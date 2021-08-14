import json
from django.template.loader import render_to_string
from followup.tasks import send_email_task
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from django.http import JsonResponse, request, response
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect, HttpResponse, redirect
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models
from django.contrib import messages
from organization.models import Organization
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from quote.models import Quote

class FollowUpCreate(CreateView):
    """
        create view for followup 
    """

    model = models.FollowUP
    fields = [
        'content'
    ]

    template_name = 'followup/followup_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['pk'] = self.kwargs.get('pk', None)
        return context

    def form_valid(self, form):
        form.instance.user= self.request.user
        form.instance.organization = Organization.objects.get(pk=self.get_context_data().get('pk'))
        self.object = form.save()

        return JsonResponse(
            data={
                'success':True
            },
            status=200)


class FollowUpList(ListView):
    """
        show followup list
    """

    queryset = models.FollowUP.objects.all()

    def filter_organization(self, request):
        organization_id = request.GET.get('organization_id')
        organization = Organization.objects.get(pk=organization_id)
        qs = models.FollowUP.objects.filter(organization=organization)
        return qs

def followup_list(request, pk):
    """
        show followup list
    """
    organization = get_object_or_404(klass=Organization, pk=pk)
    qs = models.FollowUP.objects.filter(
        organization=organization, user=request.user)

    return render(request=request,
    context={
        'object_list':qs
    }, 
    template_name='followup/followup_list.html'
    )





def email(request, pk):
    """
        send quote to the organization email
    """
    quote_instance = get_object_or_404(klass=Quote, pk=pk)
    sender = request.user.username
    body = render_to_string(template_name='quote/quote_detail.html', context={'object': quote_instance})
    receiver = quote_instance.organization.email
    send_email_task(body, receiver, sender)
    messages.success(request, 'email sent successfuly')
    return redirect(reverse_lazy('quote:quote-list'))