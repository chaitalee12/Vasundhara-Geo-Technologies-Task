from django.urls import path 
from .views import export_users 

urlpatterns = [ 
path('export-users/', export_users, name='export_users'), 
]
