from django import forms
from . import models


class FollwUpForm(forms.ModelForm):

    class Meta:
        model = models.FollowUP
        fields = (
            'title',
            'content',
            'organization',
        )