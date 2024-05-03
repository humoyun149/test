from django.urls import path

from apps import views

urlpatterns = [
    path('', views.PeopleListView.as_view(), name='index_view'),
    path('register/', views.register_view, name='register_view'),
    path('login/', views.UserLoginView.as_view(), name='login_view'),
    path('detail/<int:pk>/', views.detail_view, name='detail_view'),
    path('send/', views.send_email_to_user, name='logout_page'),

]
