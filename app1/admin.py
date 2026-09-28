from django.contrib import admin

# Register your models here.
from app1.models import student
class student_admin(admin.ModelAdmin):
    list_display=['std_id','std_name','std_age','email','Mobile']
admin.site.register(student,student_admin)    