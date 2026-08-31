#urls.py

from django.urls import path
from . import views

urlpatterns = [

    # READ - list of students
    path("", views.home, name="home"),

    # CREATE - add page
    path("add/", views.add_student, name="add_student"),

    # UPDATE - edit page
    path(
        "update/<int:student_id>/",
        views.update_student,
        name="update_student"
    ),

    path("about/", views.about, name="about"),

    path("contact/", views.contact, name="contact"),
]