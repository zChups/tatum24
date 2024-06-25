from django.urls import path
from ratings.views import RateSnippetView, TopRatedSnippetsView

urlpatterns = [
    path('<int:pk>/', RateSnippetView, name='rate_snippet'),
    path('snippets', TopRatedSnippetsView, name='top_rated_snippets'),
]
