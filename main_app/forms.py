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

# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'media_file']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
