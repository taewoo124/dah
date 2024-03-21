from django.urls import path

import dashboard.views as views

app_name = 'dashboard'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('delete/<int:post_id>', views.delete_post, name='delete_post'),
]
