from django.contrib import admin
from . import models as m


class Group_Member_In_Line(admin.TabularInline):
    model = m.Group_Members

    
admin.site.register(m.Group)
