from django.urls import path

from apps import views

urlpatterns = [
    path('', views.index_views, name='index')
]