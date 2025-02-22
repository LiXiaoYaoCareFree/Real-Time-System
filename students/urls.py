from django.urls import path, include
from students.views import StudentListView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
]