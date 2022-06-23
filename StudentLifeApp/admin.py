from django.contrib import admin
from .models import students  # new
# Register your models here.
@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'ageGroup', 'year', 'area']