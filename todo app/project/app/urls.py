from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_user, name='delete'),
    path('update/<int:pk>/', views.update_user, name='update'),
 
]