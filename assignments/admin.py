from django.contrib import admin

from .models import Assignment, SpecifiedAssignment, Question, Choice 


admin.site.register(Assignment)
admin.site.register(SpecifiedAssignment)
admin.site.register(Question)
admin.site.register(Choice)