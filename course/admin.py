from django.contrib import admin

from course.models import Category,Course,Images
# Register your models here.
class CourseImageInline(admin.TabularInline):
    model =Images
    extra=5
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ["status"]

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','category','price','image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ["status","category"]
    inlines= [CourseImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title',"course","image"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Images,ImagesAdmin)