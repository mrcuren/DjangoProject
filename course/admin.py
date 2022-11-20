from django.contrib import admin

from course.models import Category,Course
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ["status"]

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','category','price']
    list_filter = ["status","category"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)