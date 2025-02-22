from django.urls import path, include
from grades.views import GradeListView
from grades.views import GradeCreateView
from grades.views import GradeUpdateView
from grades.views import GradeDeleteView

urlpatterns = [
    path('', GradeListView.as_view(), name='grades_list'),
    path('create/', GradeCreateView.as_view(), name='grade_create'),
    path('<int:pk>/update/', GradeUpdateView.as_view(), name='grade_update'),
    path('<int:pk>/delete/', GradeDeleteView.as_view(), name='grade_delete'),
]