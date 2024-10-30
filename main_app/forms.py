from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']


from django import forms

class NewsFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "Всі"),
        ("DR", "Draft"),
        ("PU", "Published"),
        ("AR", "Archived"),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус", widget=forms.Select(attrs={"class": "form-control"}))
