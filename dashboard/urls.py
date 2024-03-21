from django.urls import path

import dashboard.views as views

app_name = 'dashboard'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.list, name='list_with_id'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
