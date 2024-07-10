from django.urls import path
from users.views.login import LoginView, LogoutView
from users.views.profile import profile_view, profile_update_view
from users.views.signup import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update_view, name='profile_update'),
]

