from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='broadcast/auths/password_change_done.html'),
         name='password_change_done'),

    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='broadcast/auths/password_change.html',
            success_url=reverse_lazy('accounts:password_change_done')
        ),
        name='password_change'
    ),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='broadcast/auths/password_reset_done.html'),
         name='password_reset_done'),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='broadcast/auths/password_reset_confirm.html',
            success_url=reverse_lazy('accounts:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='broadcast/auths/password_reset_form.html',
             email_template_name='broadcast/auths/password_reset_email.html',
             success_url=reverse_lazy("accounts:password_reset_done")
         ),
         name='password_reset'
         ),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='broadcast/auths/password_reset_complete.html'),
         name='password_reset_complete'),
]
