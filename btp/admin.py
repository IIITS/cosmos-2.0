from django.contrib import admin
from btp.models import *

admin.site.register(Application)
admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Semester)
admin.site.register(BTPWeek)
admin.site.register(BTPEvalPanel)
admin.site.register(BTPEvalSet)
admin.site.register(BTPProjectGroup)
admin.site.register(BTPSetWeek)
admin.site.register(BTPSubmission)
admin.site.register(Resources)
admin.site.register(BTPMarks)
admin.site.register(Project)
admin.site.register(ProjectMedia)
admin.site.register(ProjectArchives)
admin.site.site_header = 'Cosmos Administrator'

