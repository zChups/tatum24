from django.views.generic import ListView
from django.contrib.auth.models import User
from django.db.models import Count

from snippets.models import Snippet


class TopAuthorsView(ListView):
    model = User
    template_name = 'snippets/templates/popular/top_authors.html'
    context_object_name = 'popular_top_authors_list'
    paginate_by = 10

    def get_queryset(self):
        # Annotate each User with the count of their snippets
        queryset = User.objects.annotate(snippet_count=Count('snippets')).order_by('-snippet_count')

        # Exclude authors with 0 snippets
        queryset = queryset.exclude(snippet_count=0)

        return queryset


class TopLanguagesView(ListView):
    model = Snippet
    template_name = 'snippets/templates/popular/top_languages.html'
    context_object_name = 'top_languages_list'
    paginate_by = 10

    def get_queryset(self):
        return Snippet.objects.values('language__name').annotate(snippet_count=Count('id')).order_by('-snippet_count')


