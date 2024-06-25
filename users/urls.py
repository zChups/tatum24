from django.urls import path

from users.views.login import LoginView, LogoutView
from users.views.profile import ProfileView
from users.views.signup import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView, name='login'),
    path('profile/', ProfileView, name='profile'),
    path('logout/', LogoutView, name='logout'),
]
