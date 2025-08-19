from django.contrib import admin
from course.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'students']
    list_display = ['title']
    search_fields = ['title']


