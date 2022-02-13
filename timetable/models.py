from django.db import models
from accounts.models import *

# Create your models here.

class CourseDetails(models.Model):
    course_code = models.CharField(max_length=8, blank=False)
    course_title = models.CharField(max_length=30, blank=False)
    course_unit = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return self.course_code
    class Meta:
        verbose_name_plural = 'CourseDetails'

class StudentTimetable(models.Model):
    VENUE = (
        ('NLT1', 'NEW LECTURE THEATRE 1'),
        ('NLT2', 'NEW LECTURE THEATRE 2'),
        ('NLT3', 'NEW LECTURE THEATRE 3'),
        ('BAS', 'BASEMENT CLASSROOM'),
    )

    WEEKDAY = (
        ('MON', 'MONDAY'),
        ('TUE', 'TUESDAY'),
        ('WED', 'WEDNESDAY'),
        ('THUR', 'THURSDAY'),
        ('FRI', 'FRIDAY'),
    )
    
    weekday = models.CharField(choices=WEEKDAY, max_length=4, blank=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ManyToManyField(CourseDetails)
    time = models.TimeField()
    venue = models.CharField(choices=VENUE,max_length=100, blank=False)

    class Meta:
        verbose_name_plural = 'StudentTimetable'

class FacultyTimeTable(models.Model):
    pass