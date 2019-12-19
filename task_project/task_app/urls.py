from django.urls import path
from task_app import views

app_name = "task_app"

urlpatterns = [
    path('search/',views.search,name="search"),
    path('upload/',views.upload,name="upload"),
    path('requested_search/', views.requested_search, name='requested_search'),
]
