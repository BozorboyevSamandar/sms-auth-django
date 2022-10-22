from django.urls import path
from .views import auth_login, confirm

urlpatterns = [
    path('login', auth_login, name='login'),
    path('confirm/<uuid:id>', confirm, name='confirm'),
]
