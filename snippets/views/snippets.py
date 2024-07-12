from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from snippets.models import Snippet
from django.contrib import messages
from snippets.forms.search_input_forms import SnippetSearchForm


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'
    context_object_name = 'snippets'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by search query 'q'
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SnippetSearchForm(self.request.GET)
        return context


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


class AddSnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        exclude = ['author']


@login_required
def AddSnippetView(request):
    if request.method == 'POST':
        form = AddSnippetForm(request.POST)
        if form.is_valid():
            new_snippet = form.save(commit=False)  # Not saved instance of snippet
            new_snippet.author = request.user
            new_snippet.save()  # Saved instance
            messages.success(request, 'Snippet created successfully')
            return redirect(new_snippet.get_absolute_url())
    else:
        form = AddSnippetForm()

    return render(request, 'snippets/templates/snippets/add_snippet.html', {'form': form})


@login_required
@require_POST
def SnippetRemoveView(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)

    if request.user == snippet.author or request.user.groups.filter(name='Moderator').exists():
        snippet.delete()
        messages.success(request, 'Snippet deleted successfully')
    else:
        messages.error(request, 'You do not have permission to delete this snippet.')
    return redirect('profile')


@login_required
def edit_snippet_view(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)

    if not (request.user == snippet.author or request.user.groups.filter(name='Moderator').exists()):
        messages.error(request, 'You do not have permission to edit this snippet.')
        return redirect(snippet.get_absolute_url())

    if request.method == 'POST':
        form = AddSnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Snippet modified successfully')
            return redirect(snippet)
        else:
            messages.error(request, 'Fill all the fields')
    else:
        form = AddSnippetForm(instance=snippet)

    return render(request, 'snippets/templates/snippets/edit_snippet.html', {'form': form})
