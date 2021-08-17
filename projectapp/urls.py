from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView

app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),

    path('list/', ProjectListView.as_view(), name='list'),
]
