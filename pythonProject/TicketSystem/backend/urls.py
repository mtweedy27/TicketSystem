import django.contrib.auth
from django.contrib import admin
from django.urls import path, include
from accounts import views as a
from officerpages import views as o

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('', include("accounts.urls")),
    path('', include("officerpages.urls")),
    path('admin/', admin.site.urls),
    path('register/', a.register, name='register'),
    path('dashboard/', o.dashboard, name='dashboard'),
]

