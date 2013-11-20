from django.contrib import admin

# Register your models here.
from database.models import Run, Configuration, Benchmark, Testfile

admin.site.register(Run)
admin.site.register(Configuration)
admin.site.register(Benchmark)
admin.site.register(Testfile)