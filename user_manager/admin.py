from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as userAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User, StudentProfile, ParentProfile, GradeDetails

# Admin Site Modifications
admin.site.site_header = "Intellects Administration"
admin.site.site_title = "Intellects"
admin.site.index_title = "Intellects Site Administration"


class StudentProfileInline(admin.StackedInline):
    model = StudentProfile


class ParentProfileInline(admin.StackedInline):
    model = ParentProfile


class UserAdmin(userAdmin):
    #inlines = [ParentProfileInline,StudentProfileInline]
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_student', 'is_parent', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'is_parent', 'is_student', 'password1', 'password2'),
        }),
    )
    

admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(ParentProfile)
admin.site.register(GradeDetails)
