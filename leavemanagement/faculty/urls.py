from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.FacultyHome, name='FacultyHome'),
    # path('login/', auth_views.LoginView.as_view(template_name='faculty/login.html', redirect_field_name='FacultyHome'),name="facultyLogin"),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='faculty/login.html', redirect_field_name='FacultyHome'),
        name="facultyLogin"
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='faculty/logout.html', redirect_field_name='FacultyHome'),
        name="facultyLogout"
    ),
    path('pending-applications/', views.PendingApplications, name='FacultyPendingApplications'),
    path('accept-application/<int:app_id>/', views.AcceptApplication, name="AcceptApplication"),
    path('reject-application/<int:app_id>/', views.RejectApplication, name="RejectApplication"),
]
