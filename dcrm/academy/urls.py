from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('new_course/', views.new_course, name='new_course'),
    path('all_courses/', views.all_courses, name='all_courses'),
]
