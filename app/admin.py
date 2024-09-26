from django.contrib import admin
from app.models import *
from employees.models import *
from django.contrib.auth.admin import UserAdmin



admin.site.register(CsInfo)
admin.site.register(Constructedschools)
admin.site.register(CsEnrollment)
admin.site.register(CsTeacherKobo)
admin.site.register(DsWiseCsList)
admin.site.register(Fieldstaffassignedcs)
admin.site.register(MneChecklist)
admin.site.register(TeacherInfo)
admin.site.register(empbasicinfo)
admin.site.register(empsalary)





# python manage.py inspectdb

