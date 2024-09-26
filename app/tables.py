import django_tables2 as tables
from .models import *

class MyTable(tables.Table):
    class Meta:
        model = TeacherInfo
        fields = ("teacher_name", "cnic", )