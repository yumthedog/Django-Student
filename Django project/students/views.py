#views.py

from django.shortcuts import render, redirect
from .models import Student


# READ - list of students
def home(request):
    students = Student.objects.all()
    return render(request, "home.html", {"students": students})


# CREATE - add a new student
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")

        student = Student(
            name=name,
            age=age,
            email=email,
            address=address
        )

        student.save()

        return redirect("home")

    return render(request, "add.html")


# UPDATE - edit an existing student
def update_student(request, student_id):

    # Find the student by ID
    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        # Replace old data with new data
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.email = request.POST.get("email")
        student.address = request.POST.get("address")

        student.save()

        return redirect("home")

    # Show the edit form with old data
    return render(request, "update.html", {"student": student})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")