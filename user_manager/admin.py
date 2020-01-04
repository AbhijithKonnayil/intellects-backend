from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as userAdmin
from .models import User, StudentProfile, ParentProfile
# Register your models here.


class StudentProfileInline(admin.TabularInline):
    model = StudentProfile


class ParentProfileInline(admin.TabularInline):
    model = ParentProfile


class UserAdmin(userAdmin):
    inlines = [StudentProfileInline, ParentProfileInline]


admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(ParentProfile)
