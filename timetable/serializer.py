# from RB_Backend.rb_backend.result_broadsheet.models import Department
# from RB_Backend.rb_backend.result_broadsheet.serializers import DepartmentSerializer
from rest_framework import serializers
from . import models

#write your serializers here
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = "__all__"
        
def serializeFaculty(FacultyOb, many=False):
    if many is not False:
        serializer = FacultySerializer(FacultyOb, many=True)
        return serializer.data
    else:
        serializer = FacultySerializer(FacultyOb)
        return serializer.data
    
    
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"
        
def serializeDepartment(Deptob, many=False):
    if many is not False:
        serializer = DepartmentSerializer(Deptob, many=True)
        return serializer.data
    else:
        serializer = DepartmentSerializer(Deptob)
        return serializer.data 
    
    
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Level
        fields = "__all__"
        
def serializeLevel(Levelob, many=False):
    if many is not False:
        serializer = LevelSerializer(Levelob, many=True)
        return serializer.data
    else:
        serializer = LevelSerializer(Levelob)
        return serializer.data
    
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"
        
def serializeRole(Roleob, many=False):
    if many is not False:
        serializer = LevelSerializer(Roleob, many=True)
        return serializer.data
    else:
        serializer = LevelSerializer(Roleob)
        return serializer.data
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"
        
def serializeStudent(Studentob, many=False):
    if many is not False:
        serializer = LevelSerializer(Studentob, many=True)
        return serializer.data
    else:
        serializer = LevelSerializer(Studentob)
        return serializer.data
    
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Session
        fields = "__all__"
        
def serializeSession(Sessionob, many=False):
    if many is not False:
        serializer = LevelSerializer(Sessionob, many=True)
        return serializer.data
    else:
        serializer = LevelSerializer(Sessionob)
        return serializer.data
    
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = "__all__"
        
def serializeStaff(Staffob, many=False):
    if many is not False:
        serializer = LevelSerializer(Staffob, many=True)
        return serializer.data
    else:
        serializer = LevelSerializer(Staffob)
        return serializer.data
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"
        
def serializeCourse(Courseob, many=False):
    if many is not False:
        serializer = LevelSerializer(Courseob, many=True)
        return serializer.data
    else:
        serializer = LevelSerializer(Courseob)
        return serializer.data
    
class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venue
        fields = "__all__"
        
def serializeVenue(Venueob, many=False):
    if many is not False:
        serializer = LevelSerializer(Venueob, many=True)
        return serializer.data
    else:
        serializer = LevelSerializer(Venueob)
        return serializer.data
    
class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"
        
def serializeTimetable(Timetableob, many=False):
    if many is not False:
        serializer = LevelSerializer(Timetableob, many=True)
        return serializer.data
    else:
        serializer = LevelSerializer(Timetableob)
        return serializer.data
