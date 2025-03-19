from django.urls import path

from .views import views
from .views import auth_views, account_views



urlpatterns = [
    path('register/', auth_views.register_user, name='register'),
    path('logout', auth_views.user_logout, name='logout'),
    path('login/', auth_views.user_login, name="login"),
    path('', views.profiles, name = 'profiles'),
    path("profile/<str:pk>/", views.profile, name = "user-profile" ),
    path('user_account', account_views.user_account, name='user_account'),
]
