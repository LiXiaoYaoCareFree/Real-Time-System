from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from grades.models import Grade
from django.template.loader import get_template
from django.db.models import Q
from django.urls import reverse_lazy

from grades.forms import GradeForm
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
    

class GradeCreateView(CreateView):
    model = Grade
    template_name = 'grades/grade_form.html'
    form_class = GradeForm
    success_url = reverse_lazy('grades_list')



class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'grades/grade_form.html'
    form_class = GradeForm
    success_url = reverse_lazy('grades_list')

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grades/grade_delete_confirm.html'
    success_url = reverse_lazy('grades_list')
