from snippets.models import Snippet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def ProfileView(request):
    user = request.user
    snippets = Snippet.objects.filter(author=user)
    return render(request, 'users/profile.html', {'user': user, 'snippets': snippets})
