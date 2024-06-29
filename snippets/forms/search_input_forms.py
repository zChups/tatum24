from django import forms


class SnippetSearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
