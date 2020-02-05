from django.contrib import admin
from .models import SemesterPack, CoursePack, ModulePack, QuestionPack

admin.site.register(SemesterPack)
admin.site.register(CoursePack)
admin.site.register(ModulePack)
admin.site.register(QuestionPack)
