from django.db.models import Count
from snippets.models import Snippet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from bookmarks.models import Bookmark


@login_required
def AddBookmarkView(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    try:
        Bookmark.objects.get(user=request.user, snippet=snippet)
    except Bookmark.DoesNotExist:
        Bookmark.objects.create(user=request.user, snippet=snippet)
    messages.success(request, 'Snippet bookmarked successfully')
    return HttpResponseRedirect(snippet.get_absolute_url())


@login_required
def DeleteBookmarkView(request, snippet_id):
    if request.method == "POST":
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        Bookmark.objects.filter(user=request.user, snippet=snippet).delete()
        messages.success(request, 'Snippet not bookmarked successfully')
        return HttpResponseRedirect(snippet.get_absolute_url())
    else:
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        return render(request, 'bookmarks/templates/bookmark/confirm_bookmark_delete.html', {'snippet': snippet})


class UserBookmarksListView(ListView):
    model = Bookmark  # Set the model for the ListView
    template_name = 'bookmarks/templates/bookmark/user_bookmarks.html'  # Template to render
    context_object_name = 'bookmarks'  # Context variable name in template
    paginate_by = 10  # Number of bookmarks per page

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        # Custom logic to handle non-logged-in users
        if not request.user.is_authenticated:
            # Redirect non-logged-in users to a different view or URL
            # Example: Redirect to a login page with a custom message
            return redirect('login')

        return super().dispatch(request, *args, **kwargs)


class MostBookmarkedView(ListView):
    model = Snippet
    template_name = 'bookmarks/templates/bookmark/most_bookmarked.html'
    context_object_name = 'most_bookmarked_list'
    paginate_by = 10

    def get_queryset(self):
        # Annotate each Snippet with the count of their bookmarks
        queryset = Snippet.objects.annotate(bookmark_count=Count('bookmarks')).order_by('-bookmark_count')
        return queryset[:3]  # Limiting to the first three most bookmarked snippets

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add other context variables for pagination if needed
        return context
