from snippets.models import Snippet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def ProfileView(request):
    user = request.user
    if user.groups.filter(name='Moderator').exists():
        snippets = Snippet.objects.all().order_by('author__username')  # Order by author's username
        return render(request, 'users/templates/profile/moderator-profile.html', {'user': user, 'snippets': snippets})
    else:
        snippets = Snippet.objects.filter(author=user)
        return render(request, 'users/templates/profile/normal-profile.html', {'user': user, 'snippets': snippets})


