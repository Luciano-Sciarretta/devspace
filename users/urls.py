from django.urls import path
from .views import views
from .views import auth_views, account_views, skill_views, messages_views



urlpatterns = [
    path('register/', auth_views.register_user, name='register'),
    path('logout', auth_views.user_logout, name='logout'),
    path('login/', auth_views.user_login, name="login"),
    path('', views.profiles, name = 'profiles'),
    path("profile/<str:pk>/", views.profile, name = "user-profile" ),
    path('user-account/', account_views.user_account, name='user-account'),
    path('edit-account/', account_views.edit_account, name='edit-account'),
    path('create-skill/', skill_views.create_skill, name='create-skill'),
    path('update-skill/<str:pk>/', skill_views.update_skill, name='update-skill'),
    path('delete-skill/<str:pk>', skill_views.delete_skill, name='delete-skill'),
    path('inbox/', messages_views.inbox, name = 'inbox'),
    path( 'message/<str:pk>/', messages_views.single_message , name = 'message'),
    path('send-message/<str:pk>', messages_views.create_message, name='send-message')
]
