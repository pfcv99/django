from django.urls import path
from .import views
urlpatterns = [
    path('', views.addstudents, name="add_students"),
    path('update/<str:id>/', views.edit, name="edit"),
    path('delete/<str:id>/', views.deletestudents, name="delete_students"),
]