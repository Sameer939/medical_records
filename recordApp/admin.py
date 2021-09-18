from django.contrib import admin
from .models import Doctor, Students

class StudentInline(admin.TabularInline):
    model = Students
    extra = 0

class DoctorAdmin(admin.ModelAdmin):
    inlines = [StudentInline]



admin.site.register(Doctor, DoctorAdmin)

# Register your models here.
