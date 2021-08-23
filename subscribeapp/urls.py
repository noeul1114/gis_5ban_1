from django.urls import path

from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]
