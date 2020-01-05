from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as userAdmin
from .models import User, StudentProfile, ParentProfile

#Admin Site Modifications
admin.site.site_header="Intellects Administration"
admin.site.site_title = "Intellects"
admin.site.index_title = "Intellects Site Administration"


class StudentProfileInline(admin.TabularInline):
    model = StudentProfile


class ParentProfileInline(admin.StackedInline):
    model = ParentProfile


class UserAdmin(userAdmin):
    inlines = [StudentProfileInline, ParentProfileInline]


admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(ParentProfile)
