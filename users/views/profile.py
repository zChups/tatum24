from snippets.models import Snippet
from users.forms.modify_profile_form import UserProfileForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.models import Profile


@login_required
def profile_view(request):
    user = request.user
    if user.groups.filter(name='Moderator').exists():
        snippets = Snippet.objects.all().order_by('author__username')
        return render(request, 'users/templates/profile/moderator_profile.html', {'user': user, 'snippets': snippets})
    else:
        snippets = Snippet.objects.filter(author=user)
        return render(request, 'users/templates/profile/normal_profile.html', {'user': user, 'snippets': snippets})


@login_required
def profile_update_view(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error while updating profile')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile/profile_update.html', {'form': form})
