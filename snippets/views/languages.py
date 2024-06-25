from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from snippets.models import Language


class LanguageListView(ListView):
    model = Language
    paginate_by = 20
    template_name = 'snippets/templates/languages/language_list.html'
    context_object_name = 'languages'


class LanguageDetailView(DetailView):
    model = Language
    template_name = 'snippets/templates/languages/language_detail.html'
    context_object_name = 'language'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snippets'] = self.object.snippets.all()
        return context
