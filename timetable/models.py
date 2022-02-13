from django.db import models

# Create your models here.

class CourseDetails(models.Model):
    course_code = models.CharField(max_length=8, blank=False)
    course_title = models.CharField(max_length=30, blank=False)

    def __str__(self) -> str:
        return self.course_code
    class Meta:
        verbose_name_plural = 'CourseDetails'

class Timetable(models.Model):
    course = models.ManyToManyField(CourseDetails)
    venue = models.CharField(max_length=23)

    class Meta:
        verbose_name_plural = 'Timetable'