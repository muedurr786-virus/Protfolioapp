from django.urls import path
from .views import *

urlpatterns = [
    # Authentication
    path('register/', registerpage, name='register'),
    path('', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),

    # Dashboard
    path('dashboard/', dashboardPage, name='dashboard'),

    path('dashboard/', dashboardPage, name='dashboard'),
    path('dashboard/personalinfo/', personalinfo_page, name='personalinfo'),
    path('dashboard/project/', project_page, name='project'),
    path('dashboard/technical/', technical_page, name='technical'),
    path('dashboard/experience/', experience_page, name='experience'),
    path('dashboard/education/', education_page, name='education'),
]

