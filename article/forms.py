from django import forms
from article.models import Rassilka, Topics


class ItemChangeListForm(forms.ModelForm):

    # here we only need to define the field we want to be editable
    them = forms.ModelMultipleChoiceField(queryset=Topics.objects.all(),
        required=False)