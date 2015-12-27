from django.conf.urls import url
import views

urlpatterns = [
    url(r'^create-course/', views.create_course),
    url(r'^create-teacher/', views.create_teacher),
    url(r'^create-student/', views.create_student),
    url(r'^course-register/', views.course_register),
    url(r'^list-teacher/', views.list_teacher),
    url(r'^list-student/', views.list_student),
    url(r'^list-course/', views.list_course),
]
