from django.shortcuts import render
from django.views.generic import ListView
from grades.models import Grade
from django.template.loader import get_template
# Create your views here.

class GradeListView(ListView):
    model = Grade
    template_name = 'grades/grades_list.html'
    filed = ['grade_name', 'grade_number']
    context_object_name = 'grades'
