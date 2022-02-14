from django.db import models
# This is used for translation
from django.utils.translation import deactivate, gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from  accounts import models as a_models


# Create your models here.

class Faculty(models.Model):
    faculty_name =models.CharField(max_length=200, blank=False)
    faculty_code = models.CharField(max_length=10, blank=False)

    def __str__(self) -> str:
        return self.faculty_name

class Department(models.Model):
    dept_name = models.CharField(max_length=150, blank=False)
    dept_code = models.CharField(max_length=10, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.dept_name

class Level(models.Model):
    level_name = models.IntegerField( blank=False)

    def __str__(self) -> str:
        return str(self.level_name) + " Level"
    class Meta:
        verbose_name_plural = "Level"

class Role(models.Model):
    role_name =models.CharField(max_length=30, blank=True)
    role_code = models.CharField(max_length=3, blank=True)
    class Meta:
        verbose_name_plural = "Role"

# Can you please add department as part of the fields
class Student(models.Model):
    user = models.OneToOneField(a_models.User, on_delete=models.CASCADE)
    mat_no = models.CharField(max_length=20, blank=False, unique=True)
    level = models.ForeignKey(Level, blank=False, default=0, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return  self.user.first_name + " "+self.user.other_names[0]+". "+self.user.last_name+" "+str(self.level)

    class Meta:
        verbose_name_plural = 'Student'

class Session(models.Model):
    session_name = models.CharField(max_length=100, null=True, unique=True)
    session_start = models.DateField(null=True)
    session_end = models.DateField(null=True)

    def __str__(self) -> str:
        return  self.session_name+" Session"

class Staff(models.Model):
    user = models.OneToOneField(a_models.User, on_delete=models.CASCADE)
    staff_number = models.CharField(max_length=20, blank=False, default="")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Staff'

class Course(models.Model):
    STATUSES=(
        ('A','Approved' ),
        ('D', 'Discontinued')
    )
    SEMESTER=(
        ('F','First Semester' ),
        ('S', 'Second Semester')
    )
    course_name = models.CharField(max_length=200, blank=False)
    course_code = models.CharField(max_length=50, blank=False, unique =True)
    credit_unit = models.IntegerField(blank=False)
    c_a_score = models.IntegerField(blank=True, default=0)
    exam_score = models.IntegerField(blank=True, default=0)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.CharField(choices=SEMESTER, max_length=1)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES, blank=False)
    lecturer = models.ForeignKey(Staff, on_delete=models.CASCADE, default = None, null =True)
    general =models.BooleanField(default=False)

    def __str__(self) -> str:
        return "("+self.course_code+") "+self.course_name

    class Meta:
        verbose_name_plural = "Course"

class Grade(models.Model):
    grade_code = models.CharField(max_length=2, blank=False)
    grade_point = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return self.grade_code+" ("+str(self.grade_point)+")"

# class Remark(models.Model):
#     pass
class Result(models.Model):
    SEMESTER=(
        ('F','First Semester' ),
        ('S', 'Second Semester')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    c_a_score = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0)
    exam_score = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0)
    grade = models.ForeignKey(Grade, default=6, on_delete=models.CASCADE)
    # remark = models.ForeignKey()
    semester = models.CharField(max_length=1, choices=SEMESTER, blank=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default="")
    cleared = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "("+str(self.session)+") "+str(self.student.mat_no)+" ("+str(self.course.course_code)+" | "+str(self.grade)+")"
    class Meta:
        unique_together = ('student', 'course', 'session')