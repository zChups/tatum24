from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from tatum24.views import HomeView

urlpatterns = [
    path('', HomeView, name='home'),
    path('admin/', admin.site.urls),
    path('snippets/', include('snippets.urls')),
    path('rates/', include('ratings.urls')),
    path('bookmarks/', include('bookmarks.urls')),
    path('accounts/', include('users.urls')),
]


