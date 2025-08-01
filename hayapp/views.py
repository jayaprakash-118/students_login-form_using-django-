from django.shortcuts import render, redirect
from .models import student

# Home Page View
def home(request):
    return render(request, 'home.html')

# Student List View
def student_list(request):
    students = student.objects.all()
    return render(request, 'studentslist.html', {'students': students})

# Add Student View
def add_student(request):
    if request.method == 'POST':
        stu_name = request.POST.get('stu_name')
        rollno = request.POST.get('rollno')
        year = request.POST.get('year')
        birthdate = request.POST.get('birthdate')
        email = request.POST.get('email')
        course = request.POST.get('course')
        photo = request.FILES.get('photo') 


        student.objects.create(        ## saving the data into databbase
            stu_name=stu_name,
            rollno=rollno,
            year=year,
            birthdate=birthdate,
            email=email,
            course=course,
            photo=photo
        )
        return redirect('studentslist')  # Redirect to student list page after adding

    return render(request, 'addstudent.html')
