from django import forms
from .models import News

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'forms-control'}),
            'content':forms.Textarea(attrs={'class':'forms-control', 'rows': 5}),
            'category': forms.Select(attrs={'class':'forms-control'}),
        }