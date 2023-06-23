from django.urls import path
from subapp import  views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.log_out,name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('item_save', views.item_save, name='item_save'),
    path('item_edit/<pk>', views.item_edit, name='item_edit'),
    path('item_delete/<pk>', views.item_delete, name='item_delete'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_profile_save', views.user_profile_save, name='user_profile_save'),
    path('user_view', views.user_view, name='user_view'),
    path('user_create', views.user_create, name='user_create'),
]