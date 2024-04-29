from django.urls import path

from apps import views
from apps.views import BlogListView

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='blog_list'),
    path('products', views.BlogListView.as_view(), name='product-list'),
    path('detail/<int:pk>/', views.detail_view, name='detail_view'),
    path('register/', views.register_view, name='register_view'),
    path('', views.CustomLoginView.as_view(), name='login_view'),
]



