from django.urls import path, include
from grades.views import GradeListView

urlpatterns = [
    path('', GradeListView.as_view(), name='grades_list'),
]