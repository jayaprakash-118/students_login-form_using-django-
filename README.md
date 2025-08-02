# 🎓 Student Login System using Django

This is a simple **Student Login and Management System** built with **Python Django**, using **HTML for frontend**, **SQLite for the database**, 
and **Django Models, Views, and Templates** for backend logic.

It allows adding, listing, and managing student records — a great beginner-level Django project to understand how models, forms, and views work together.

## 📌 Features

✅ Add Student Form  
✅ View List of Students  
✅ Store Student Data in SQLite  
✅ Backend Logic with Django Views  
✅ HTML + CSS Templates  
✅ Django Admin Panel


## 🛠️ Technologies Used

- Python 
- Django 
- SQLite (default Django database)
- HTML5 / CSS3


## 📂 Project Structure

students_login-form_using-django-/        ← GitHub repo root
├── student/                              ← Django project folder (main settings)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                       ← Configuration: media, static, apps
│   ├── urls.py                           ← Main URL router
│   └── wsgi.py
│
├── studentapp/                           ← Your main Django app
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/                        ← HTML templates
│   │   ├── home.html
│   │   ├── student_list.html
│   │   └── add_student.html
│   ├── static/                           ← Static files (CSS/images/js if any)
│   │   └── studentapp/
│   │       └── styles.css
│   ├── admin.py                          ← Register model in admin
│   ├── apps.py
│   ├── forms.py                          ← Student form (if using ModelForm)
│   ├── models.py                         ← Student model with ImageField
│   ├── tests.py
│   ├── urls.py                           ← App-specific URLs
│   └── views.py                          ← Add/list logic here
│
├── media/                                ← Uploaded student photos (ImageField)
│   └── (image files like student1.jpg, student2.png, etc.)
│
├── db.sqlite3                            ← SQLite database file
├── manage.py
├── README.md                             ← Your GitHub project description
└── requirements.txt                      ← (Optional) Python package list


---

## ⚙️ How to Run This Project Locally

Follow these steps to set up and run the project on your local machine:

###  1. Clone the Repository

bash or cmd
git clone https://github.com/jayaprakash-118/students_login-form_using-django-.git
cd students_login-form_using-django-

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

3. Install Dependencies
  - pip install django
 4. Apply Migrations
    python manage.py makemigrations
    python manage.py migrate

5. (Optional) Create a Superuser
    python manage.py createsuperuser
   
7. Run the Development Server
   python manage.py runserver

# Home page





