from django import forms
from models import *


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        exclude = []


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = []


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        exclude = ['teacher', 'studens']


class CourseRegisterForm(forms.Form):
    pass
