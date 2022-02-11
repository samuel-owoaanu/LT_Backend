from django.db import models

# Create your models here.

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50)

class Department(models.Model):
    department_name = models.CharField(max_length=30)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Student(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    other_name = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=2, blank=False)
    level = models.CharField(max_length=10, blank=False)


class Lecturer(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    other_name = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=2, blank=False)
    level = models.CharField(max_length=10, blank=False)