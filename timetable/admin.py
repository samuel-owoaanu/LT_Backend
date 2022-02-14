from django.contrib import admin
from .models import *
# Register your models here.

 
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Role)
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Venue)
admin.site.register(Timetable)


# class CourseDetailsAdmin(admin.ModelAdmin):
#     list_display = ('course_code', 'course_title',)
#     search_fields = ('course_code', 'course_title',)

# admin.site.register(CourseDetails, CourseDetailsAdmin)
# admin.site.register(StudentTimetable)

