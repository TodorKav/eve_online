from django.urls import path
from eve.industry import views
urlpatterns = [
    path('', views.Test.as_view(), name='test'),
]