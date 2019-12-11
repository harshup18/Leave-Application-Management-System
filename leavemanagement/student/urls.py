from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.StudentHome, name='StudentHome'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='student/login.html', redirect_field_name='StudentHome'),
        name="studentLogin"
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='student/logout.html', redirect_field_name='StudentHome'),
        name="studentLogout"
    ),
    path('create-new-application', views.NewStudentApplication, name='NewApplication'),
    path('pending-application', views.PendingApplication, name='StudentPendingApplication'),
    path('archived-application', views.ArchivedApplication, name='StudentArchivedApplication'),
]
