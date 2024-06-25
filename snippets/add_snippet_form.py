from django import forms
from snippets.models import Snippet


class AddSnippetForm(forms.ModelForm):
    tags = forms.CharField(max_length=255)

    class Meta:
        model = Snippet
        fields = ['title', 'description', 'code', 'language']
        widgets = {
            'description': forms.Textarea,
            'code': forms.Textarea,
        }

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super(AddSnippetForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        snippet = super(AddSnippetForm, self).save(commit=False)
        snippet.tags = self.cleaned_data['tags']
        snippet.author = self.author

        if commit:
            snippet.save()
        return snippet

