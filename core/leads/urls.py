from django.urls import path
from .views import dialogflow_webhook

urlpatterns = [
    path('webhook/', dialogflow_webhook),
]