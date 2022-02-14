from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from .models import *
from .serializer import *

REQ_ERRORS = {
    """[A Dictionary of Request-Response Errors]"""

    "INVALID": {'Error': 'invalid request!!!'},
    "DATA_EXISTS": {'Error': 'Data Exists!'},
}

class FacultyData(APIView):
    def get(self, request, fa_code=None):
        faculty_data = {}
        
        if fa_code is not None:
            FacultyOb = Faculty.objects.get(faculty_code=fa_code)
            faculty_ = serializeFaculty(FacultyOb)
            faculty_data['data'] = "Faculty Detail"
            faculty_data['details'] = faculty_
            return Response(faculty_data)
        
        facultyOb = Faculty.objects.all()
        faculties = serializeFaculty(facultyOb, many=True)
        faculty_data['data'] = "Faculty List"
        faculty_data['details'] = faculties
        return Response(faculty_data)
    
    def post(self, request, fa_code=None):
        if fa_code is not None:
            facultyob = Faculty.objects.get(faculty_code=fa_code)
            serializer = FacultySerializer(facultyob, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(REQ_ERRORS['INVALID'])
        else:
            serializer = FacultySerializer(data=request.data)
            if serializer.is_valid():
                try :
                    facultyob = Faculty.objects.get(faculty_code = request.data['faculty_code'])
                    if facultyob:
                        return Response(REQ_ERRORS['DATA_EXISTS'])
                except Faculty.DoesNotExist:
                    serializer.save()
                    return Response(serializer.data)
            else:
                return Response(REQ_ERRORS['INVALID'])

    def delete(self, request, fa_code=None):
        if fa_code is not None:
            facultyOBJ = Faculty.objects.get(faculty_code=fa_code)
            serializer = FacultySerializer(facultyOBJ, data=request.data)

            if serializer.is_valid():
                serializer.delete()
                return Response(serializer.data)
            else:
                return Response(REQ_ERRORS['INVALID'])

        else:
                return Response(REQ_ERRORS['INVALID'])
            
class DepartmentData(APIView):
    def get(self, request, dep_code=None):
        if dep_code is not None:
            
            dep_code = str(dep_code.upper())
            deptobj = Department.objects.get(dept_code=dep_code)
            department_ = serializeDepartment(deptobj)
            
            return Response(department_)
        else:
            depts_dict={
                "data":"List of Departments by Faculty",
                "dept_data":list()
            }

            dept_data = list()
            deptobj = Department.objects.all()
            departments = serializeDepartment(deptobj, many=True)

            facultyobj = Faculty.objects.all()
            faculties = serializeFaculty(facultyobj, many=True)

            for faculty in faculties:
                dept={}
                dept['faculty']=faculty['faculty_name']
                dept['faculty_code']=faculty['faculty_code']
                dept['departments']=list()

                for department in departments:
                    if department['faculty']== faculty['id']:
                        dept['departments'].append(str(department['dept_name']+" ("+department['dept_code']+")"))
                dept_data.append(dept)

            depts_dict['dept_data']=dept_data
            return Response(depts_dict)
        
    def post(self, request, pk=None):
        pass

    def delete(self, request, pk=None):
        pass
    
class LevelData(APIView):
    def get(self, request, l_code=None):
        levelobj = Level.objects.all()
        levels = serializeLevel(levelobj, many=True)
        return Response(levels)

    def post(self, request, l_code=None):
        pass
    
class RoleData(APIView):
    def get(self, request, r_code=None):
        Roleobj = Role.objects.all()
        roles = serializeRole(Roleobj, many=True)
        return Response(roles)
    
class StudentData(APIView):
    def get(self, request, stu_code=None):
        Studobj = Student.object.all()
        students = serializeStudent(Studobj, many=True)
        return Response(students)
    
    
class SessionData(APIView):
    def get(self, request, ses_code=None):
        Sessionobj = Session.object.all()
        sessions = serializeSession(Sessionobj, many=True)
        return Response(sessions)
    
class StaffData(APIView):
    def get(self, request, staff_code=None):
        Staffobj = Staff.object.all()
        staff = serializeSession(Staffobj, many=True)
        return Response(staff)
    
class CourseData(APIView):
    def get(self, request, course_code=None):
        courseobj = Course.object.all()
        courses = serializeCourse(courseobj, many=True)
        return Response(courses)
    
class VenueData(APIView):
    def get(self, request, venue_code=None):
        venueobj = Venue.object.all()
        venues = serializeVenue(venueobj, many=True)
        return Response(venues)
    
class TimetableData(APIView):
    def get(self, request, timetable_code=None):
        ttobj = Session.object.all()
        tts = serializeSession(ttobj, many=True)
        return Response(tts)
