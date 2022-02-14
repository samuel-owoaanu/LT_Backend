from django.urls import path
from . import views
urlpatterns = [
    path('faculty/', views.FacultyData.as_view(), name='faculties'),
    path('department/', views.DepartmentData.as_view(), name ='departments'),
    path('level/', views.LevelData.as_view(), name = 'level'),
    path('role/', views.RoleData.as_view(), name = 'role'),
    path('Student/', views.StudentData.as_view(), name = 'student'),
    path('session/', views.SessionData.as_view(), name = 'session'),
    path('staff/', views.StaffData.as_view(), name = 'staff'),
    path('course/', views.CourseData.as_view(), name = 'course'),
    path('venue/', views.VenueData.as_view(), name = 'venue'),
    path('timetable/', views.TimetableData.as_view(), name = 'tt'),
]