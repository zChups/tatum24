from django.urls import path

from bookmarks.views import AddBookmarkView, DeleteBookmarkView, UserBookmarksListView, MostBookmarkedView

urlpatterns = [
    path('add/<int:snippet_id>/', AddBookmarkView, name='add_bookmark'),
    path('delete/<int:snippet_id>/', DeleteBookmarkView, name='delete_bookmark'),
    path('user-bookmarks/', UserBookmarksListView.as_view(), name='user_bookmarks'),
    path('most-bookmarked/', MostBookmarkedView.as_view(), name='most_bookmarked'),
]