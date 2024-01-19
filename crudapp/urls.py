from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name=''),
    path('base/',base,name='base'),
    path('create-record/',create_record),
    path('dashboard/',dashboard,name='dashboard'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('update-record/<int:pk>',update_record,name='update-record'),
    path('view-record/<int:pk>/', view_record, name='view_record'),
    path('signout/',user_logout,name='signout'),
    path('delete/<int:pk>',delete,name='delete')
]