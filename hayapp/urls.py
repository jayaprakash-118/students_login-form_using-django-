from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('studentslist/', views.student_list, name='studentslist'),  # ✅ correct view name
    path('addstudent/', views.add_student, name='addstudent'),       # ✅ correct view name
]


