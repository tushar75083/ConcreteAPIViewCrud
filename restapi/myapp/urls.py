from django.urls import path
from . import views


urlpatterns = [
    path('students/',views.StudentListCreateView.as_view()),
    path('students/<int:pk>/',views.StudentRetrieveUpdateDestroyView.as_view())
]
