from django.urls import path
from newapp import views

app_name = 'newapp'

urlpatterns = [
    path('users/', views.newuser_list),
    path('user/<int:pk>/', views.newuser_detail),
]