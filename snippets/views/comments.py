# snippets/home.py
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from snippets.models import Snippet, Comment
from snippets.forms.add_comment_form import CommentForm


@login_required
def add_comment_view(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.snippet = snippet
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added successfully.')
        else:
            messages.error(request, 'Failed to add comment. Please check the form.')

    return redirect('snippet_detail', pk=snippet.pk)


@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the current user has permission to delete the comment
    if (request.user == comment.author or request.user.groups.filter(name='Moderator').exists() or
            request.user == comment.snippet.author):
        comment.delete()
        messages.success(request, 'Comment deleted successfully')
    else:
        messages.error(request, 'You do not have permission to delete this comment.')

    # Redirect to an appropriate page after deletion attempt (e.g., back to snippet detail)
    return redirect('snippet_detail', pk=comment.snippet.pk)
