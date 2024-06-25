# views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django import forms
from snippets.models import Snippet
from django.contrib import messages

from snippets.search_input_forms import SnippetSearchForm


# Define the SnippetForm within the signup_form.py file for better organization
class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        exclude = ['author']


# ListView to display a list of snippets
class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'
    context_object_name = 'snippets'
    paginate_by = 20  # Optional: to paginate the snippets

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SnippetSearchForm(self.request.GET)
        return context


# DetailView to display a single snippet
class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/templates/snippets/snippet_detail.html'
    context_object_name = 'snippet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        snippet = self.get_object()
        context['user'] = self.request.user
        if self.request.user.is_authenticated:
            context['bookmarked'] = self.request.user.bookmarks.filter(snippet=snippet).exists()
        else:
            context['bookmarked'] = False
        return context


# View to handle adding a new snippet

@login_required
def AddSnippetView(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            new_snippet = form.save(commit=False)
            new_snippet.author = request.user  # Assign the current user as the author
            new_snippet.save()
            messages.success(request, 'Snippet created successfully')
            return redirect(new_snippet.get_absolute_url())
    else:
        form = SnippetForm()

    return render(request, 'snippets/templates/snippets/add_snippet.html', {'form': form})


@login_required
@require_POST
def SnippetRemoveView(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    # Check if the current user has permission to delete the snippet
    if request.user == snippet.author:
        snippet.delete()
        messages.success(request, 'Snippet deleted successfully')
    # Redirect to the snippet list page after deletion
    return redirect('profile')


@login_required
def EditSnippetView(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)

    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Snippet modified successfully')
            return redirect('snippet_detail', pk=snippet.pk)  # Redirect to detail view
    else:
        form = SnippetForm(instance=snippet)

    return render(request, 'snippets/templates/snippets/edit_snippet.html', {'form': form})
