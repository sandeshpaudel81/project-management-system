from django.contrib import admin
from mgmtapp.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
admin.site.register(Meeting)