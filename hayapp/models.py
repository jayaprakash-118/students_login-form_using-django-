from django.db import models



class student(models.Model):
    stu_name = models.CharField(max_length = 200)
    rollno= models.CharField(unique=True)
    year=models.IntegerField()
    birthdate=models.DateField()
    email=models.EmailField(unique=True)
    course=models.CharField()
    photo=models.ImageField(upload_to='images/')


    def __str__(self):
        return self.stu_name
