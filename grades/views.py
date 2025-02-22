from django.shortcuts import render
from django.views.generic import ListView
from grades.models import Grade
from django.template.loader import get_template
from django.db.models import Q
# Create your views here.

class GradeListView(ListView):
    model = Grade
    template_name = 'grades/grades_list.html'
    filed = ['grade_name', 'grade_number']
    context_object_name = 'grades'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(grade_name__icontains=search) | Q(grade_number__icontains=search)
            )
        return queryset