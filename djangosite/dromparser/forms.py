from django import forms

class DromParser(forms.Form):

        link = forms.CharField(label='Ссылка', required=True, max_length=200)