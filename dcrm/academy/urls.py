from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('new_course/', views.new_course, name='new_course'),
    path('all_courses/', views.all_courses, name='all_courses'),
    path('course/<int:pk>', views.course_detail, name='course_detail'),
    path('update_course/<int:pk>', views.update_course, name='update_course'),
    path('delete_course/<int:pk>', views.delete_course, name='delete_course'),
    # path('course_attendees/<int:pk>', views.course_attendees, name='course_attendees'),
    path('course_attendees_all/<int:course_id>', views.course_attendees_all, name='course_attendees_all'),
]
