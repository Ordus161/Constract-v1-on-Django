from django.urls import path
from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('', HomeApplication.as_view(), name='home'),
    #path('area/<int:area_id>/', get_area, name='area'),
    path('area/<int:area_id>/', ApplicationByArea.as_view(), name='area'),
    #path('application/<int:application_id>/', view_application, name='view_application'),
    path('application/<int:pk>/', ViewApplication.as_view(), name='view_application'),
    #path('application/add-application/', add_application, name='add_application'),
    path('application/add-application/', CreateApplication.as_view(), name='add_application'),
]