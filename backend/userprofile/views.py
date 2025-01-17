from rest_framework import generics
from .models import StudentAlumniProfile, CompanyProfile
from .serializers import (
    StudentAlumniProfileSerializer,
    CompanySerializer,
)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status


@csrf_exempt
def get_student_alumni_profile(request, email):
    try:
        student_alumni_profile = StudentAlumniProfile.objects.get(email=email)
        # Retrieve data from the model and prepare a JSON response
        response_data = {
            "email": student_alumni_profile.email,
            "job_preference": student_alumni_profile.job_preference,
            "years_of_experience": student_alumni_profile.years_of_experience,
            "previous_employer": student_alumni_profile.previous_employer,
            "linkedin_link": student_alumni_profile.linkedin_link,
            "github_link": student_alumni_profile.github_link,
            "img_file": str(student_alumni_profile.img_file.url),
            "user_summary": student_alumni_profile.user_summary,
            "gpa": student_alumni_profile.gpa,
            "highest_degree": student_alumni_profile.highest_degree,
            "degree_subject": student_alumni_profile.degree_subject,
        }
        return JsonResponse(response_data, content_type="application/json")
    except StudentAlumniProfile.DoesNotExist:
        # Handle case where the email does not exist in the model
        return JsonResponse(
            {"error": "Student Alumni Profile not found"},
            status=404,
            content_type="application/json",
        )


class StudentAlumniProfileCreateView(generics.UpdateAPIView):
    queryset = StudentAlumniProfile.objects.all()
    serializer_class = StudentAlumniProfileSerializer
    lookup_field = "email"
    lookup_url_kwarg = "email"

    def update(self, request, *args, **kwargs):
        email = kwargs.get("email")
        try:
            instance = self.queryset.get(email=email)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StudentAlumniProfile.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            print("second part", serializer.is_valid())
            if serializer.is_valid():
                print("trying to save")
                serializer.save()
                print("saved")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt  # This is added to disable CSRF protection for demonstration purposes, you should add proper CSRF protection in production
def company_profile(request, email):
    try:
        company = CompanyProfile.objects.get(email=email)
        response_data = {
            "email": company.email,
            "name": company.name,
            "website": company.website,
            "description": company.description,
            "img_file": str(company.img_file.url),
            "company_logo": str(company.company_logo.url),
        }
        return JsonResponse(response_data, content_type="application/json")
    except CompanyProfile.DoesNotExist:
        # Handle case where the email does not exist in the model
        return JsonResponse(
            {"error": "Hiring Manager Profile not found"},
            status=404,
            content_type="application/json",
        )


class CompanyProfileCreate(generics.UpdateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "email"
    lookup_url_kwarg = "email"

    def update(self, request, *args, **kwargs):
        email = kwargs.get("email")
        try:
            instance = self.queryset.get(email=email)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CompanyProfile.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
