from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.ManagerHome, name='ManagerHome'),
    path('user-select/', views.ManagerUser,name='ManagerUser'),
    # path('media/applicatons/<str:app>/', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,},)
]


# if settings.DEBUG:
#     urlpatterns += urlpatterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.STATIC_ROOT,
#         }),
# )