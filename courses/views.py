from courses.models import Course
from courses.serializers import CourseSerializer, CoursesDetalSerializer
from rest_framework import generics


class CoursesCreateView(generics.CreateAPIView):
    serializer_class = CoursesDetalSerializer


class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CoursesDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CoursesDetalSerializer
    queryset = Course.objects.all()


class CoursesDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = CoursesDetalSerializer
    queryset = Course.objects.all()

