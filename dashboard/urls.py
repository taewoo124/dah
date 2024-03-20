from django.urls import path

import dashboard.views as views

app_name = 'dashboard'
urlpatterns = [
    path('', views.list, name='list'),
    path('<str:post_id>/', views.detail, name='detail'),
]
