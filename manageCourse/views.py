from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from forms import *
from models import *


@csrf_protect
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list-student/')
        return render(request, 'createStudent.html', {'form': form})
    return render(request, 'createStudent.html', {'form': StudentForm()})


@csrf_protect
def create_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list-teacher/')
        return render(request, 'createTeacher.html', {'form': form})
    return render(request, 'createTeacher.html', {'form': TeacherForm()})


@csrf_protect
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list-course/')
        return render(request, 'createCourse.html', {'form': form})
    return render(request, 'createCourse.html', {'form': CourseForm()})


def course_register(request):
    if request.method == "POST":
        return render()
    return render(request, 'courseRegister.html')


def list_student(request):
    return render(
        request, 'listOfStudent.html',
        {
            'students': Student.objects.all()
        }
    )


def list_teacher(request):
    return render(
        request, 'listOfTeacher.html',
        {
            'teachers': Teacher.objects.all()
        }
    )


def list_course(request):
    return render(
        request, 'listOfCourse.html',
        {
            'courses': Course.objects.all()
        }
    )
