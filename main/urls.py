from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import render_pdf_view,UserListView,user_render_pdf_view
urlpatterns=[
    path('',views.home,name='home'),
    path('accounts/register/',views.register,name='register'),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('pdf_test/', render_pdf_view, name='test-view'),
    path('users_test/', UserListView.as_view() , name='users_list'),
    path('users/<pk>/', user_render_pdf_view, name='users_pdf_view'),  
]