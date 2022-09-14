from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken import views
from .views import *

app_name = 'api'
urlpatterns = [
    path('register/', registerUser, name='register_user'),
    path('login/', views.obtain_auth_token),
    path('logout/', logoutUser, name='logout_user'),
    path('createNote/<str:token>', createNote, name='createNote'),
    path('getNotes/<str:token>', getNotes, name='getNotes'),
    path('getNote/<int:id>', getNote, name='getNote'),
    path('updateNote/<int:id>', updateNote, name='updateNote'),
    path('deleteNote/<int:id>', deleteNote, name='deleteNote'),
    path('createTask/<str:token>', createTask, name='createTask'),
    path('getTasks/<str:token>', getTasks, name='getTasks'),
    path('getTask/<int:id>', getTask, name='getTask'),
    path('updateTask/<int:id>/', updateTask, name='updateTask'),
    path('updateSubTask/<int:id>/', updateSubTask, name='updateSubTask'),
    path('checkAllSubTask/<int:id>/', checkAllSubTask, name='checkAllSubTask'),
    path('deleteTask/<int:id>/', deleteTask, name='deleteTask'),
]
