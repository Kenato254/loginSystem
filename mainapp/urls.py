from django.conf import settings
from django.conf.urls.static import static

#! Built-in Config
from django.urls import path

#! Local App Config
from mainapp import views   

app_name  = 'mainapp'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login-view'),
    path('logout-confirm/', views.Logout.as_view(), name='logout-view-confirm'),
    path('logged-out/', views.LogoutDone.as_view(), name='logout-view'),
    path('register/', views.Register.as_view(), name='register-view'),
    path('register-done/', views.RegisterDone.as_view(), name='register-done-view'),
    path('profile/', views.ProfileView.as_view(), name='profile-view'),
    path('profile/<int:pk>/update/', views.EditProfile.as_view(), name='edit-profile-view'),
    path('profile/<int:pk>/update-done/', views.EditProfileDone.as_view(), name='edit-done-view'),

    #? Password Manupulation
    path('reset-password/', views.PasswordReset.as_view(), name='reset-view'),
    path('reset-password-done/', views.PasswordResetDone.as_view(), name='reset-done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='reset-confirm'),
    path('reset-complete/', views.PasswordResetComplete.as_view(), name='reset-complete'),
    path('change/', views.PasswordChange.as_view(), name='change-view'),
    path('change-done/', views.PasswordChangeDone.as_view(), name='change-done-view'),
    
]

#! Static files urls Configuration when debug is true
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
