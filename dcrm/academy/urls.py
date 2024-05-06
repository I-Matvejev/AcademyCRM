from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('new-course/', views.new_course, name='new_course'),
    path('all-courses/', views.all_courses, name='all_courses'),
    # path('course/<int:pk>', views.course_detail, name='course_detail'),
    path('update-course/<int:pk>', views.update_course, name='update_course'),
    path('delete-course/<int:pk>', views.delete_course, name='delete_course'),
    # path('attendee-detail/<int:pk>', views.attendee_detail, name='attendee_detail'),
    path('attendees/', views.attendees, name='attendees'),
    path('course-attendees-all/<int:course_id>', views.course_attendees_all, name='course_attendees_all'),
    path('delete-attendee/<int:pk>', views.delete_attendee, name='delete_attendee'),
    path('update-attendee/<int:pk>', views.update_attendee, name='update_attendee'),
    path('course-attendees-all/<int:course_id>/add-attendee/', views.add_attendee, name='add_attendee'),
    path('save-to-pdf/<int:course_id>', views.save_to_pdf, name='save_to_pdf'),
]
