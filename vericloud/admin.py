from django.contrib import admin

from vericloud.models import  File, FileHierarchy, Limitation, Requirement, VerificationRun, VerificationResult
# Register your models here.


admin.site.register(File)
admin.site.register(FileHierarchy)
admin.site.register(Limitation)
admin.site.register(Requirement)
admin.site.register(VerificationRun)
admin.site.register(VerificationResult)