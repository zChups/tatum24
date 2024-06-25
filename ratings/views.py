from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseBadRequest

from ratings.models import Rating
from snippets.models import Snippet


@login_required
def RateSnippetView(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    user = request.user

    if request.method == 'POST':
        rating_value = request.POST.get('rating')

        # Check if the rating value is valid
        if rating_value not in [Rating.LIKE, Rating.DISLIKE]:
            return HttpResponseBadRequest("Invalid rating value")

        # Check if the user has already rated this snippet
        if snippet.has_user_rated(user):
            # Update existing rating if user has already rated
            rating = snippet.ratings.get(user=user)
            rating.rating = rating_value
            rating.save()
        else:
            # Create new rating if user has not rated before
            rating = Rating.objects.create(snippet=snippet, user=user, rating=rating_value)

        # Redirect to the snippet detail page after rating
        return redirect('snippet_detail', pk=pk)
    else:
        return HttpResponseBadRequest("Only POST method is allowed for rating snippets")


def TopRatedSnippetsView(request):
    top_snippets = Snippet.objects.annotate(total_likes=Count('ratings', filter=Q(ratings__rating='like'))).order_by(
        '-total_likes')[:10]
    context = {
        'top_snippets': top_snippets
    }
    return render(request, 'ratings/templates/top_rated_snippets.html', context)
