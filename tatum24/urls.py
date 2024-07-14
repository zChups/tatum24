from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from tatum24.views.home import HomeView

urlpatterns = [
    path('', HomeView, name='home'),
    path('admin/', admin.site.urls),
    path('snippets/', include('snippets.urls')),
    path('rates/', include('ratings.urls')),
    path('bookmarks/', include('bookmarks.urls')),
    path('accounts/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
