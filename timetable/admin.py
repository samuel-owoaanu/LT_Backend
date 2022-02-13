from django.contrib import admin
from .models import *
# Register your models here.

class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_title',)
    search_fields = ('course_code', 'course_title',)

admin.site.register(CourseDetails, CourseDetailsAdmin)
admin.site.register(Timetable)