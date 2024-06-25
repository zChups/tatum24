from django.urls import path
from snippets.views.languages import LanguageListView, LanguageDetailView
from snippets.views.popular import TopAuthorsView, TopLanguagesView
from snippets.views.snippets import SnippetListView, SnippetDetailView, AddSnippetView, SnippetRemoveView, \
    EditSnippetView

urlpatterns = [
    path('languages/<slug:slug>/', LanguageDetailView.as_view(), name='language_detail'),
    path('language_list', LanguageListView.as_view(), name='language_list'),
    path('top-languages/', TopLanguagesView.as_view(), name='tatum24_top_languages'),
    path('', SnippetListView.as_view(), name='snippet_list'),
    path('<int:pk>/', SnippetDetailView.as_view(), name='snippet_detail'),
    path('add_snippet/', AddSnippetView, name='add_snippet'),
    path('<int:pk>/remove/', SnippetRemoveView, name='snippet_remove'),
    path('<int:pk>/edit/', EditSnippetView, name='edit_snippet'),
    path('top-authors/', TopAuthorsView.as_view(), name='tatum24_top_authors'),
]
