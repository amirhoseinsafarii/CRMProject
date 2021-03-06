from django.utils.http import is_safe_url
from . import forms

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect

from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response





def login_view(request):
    """
    Login the user
    """
    user = None
    form_instance = forms.LoginForm()
    if request.method == 'POST':
        form_instance = forms.LoginForm(data=request.POST)
        if form_instance.is_valid():
            username = form_instance.cleaned_data['username']
            password = form_instance.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/')
                if is_safe_url(next_url, settings.ALLOWED_HOSTS):
                    return redirect(next_url)
                else:
                    return redirect('/')
            else:
                messages.error(request, "Username or password was incorrect. ⁉")
    return render(
        request,
        context={
            'form': form_instance,
        },
        template_name='users/login.html'
    )


# View function
def logout_view(request):
    """
    Logout the user
    """
    logout(request)
    messages.info(request, "You\'ve been logged out.")
    return redirect('')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user