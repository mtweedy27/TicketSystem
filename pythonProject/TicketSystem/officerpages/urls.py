from django.urls import path
from . import views

app_name = 'officerpages'

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("update/<Tickets_data>/", views.update, name="update"),
]