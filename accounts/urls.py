"""
This is auth module urls
"""
from django.urls import path
from . import views as auth_views
from .views import CustomUserCreate, BlacklistTokenUpdateView

app_name = 'accounts'

urlpatterns = [
    path('signup/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
]
