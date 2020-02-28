from django.urls import path
from courses import views

urlpatterns = [
    path('post/', views.CoursesCreateView.as_view()),
    path('get/', views.CourseListView.as_view()),
    path('get/<int:pk>', views.CoursesDetailView.as_view()),
    path('delete/<int:pk>', views.CoursesDestroyView.as_view()),
]
