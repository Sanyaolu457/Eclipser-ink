from django import forms
from .models import POST, Tag
from authentication.models import Participant

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # or forms.SelectMultiple
        required=False
    )

    mentions = forms.ModelMultipleChoiceField(
        queryset=Participant.objects.all(),
        required=False
    )

    class Meta:
        model = POST
        fields = ["title", "content", "tags", "mentions"]