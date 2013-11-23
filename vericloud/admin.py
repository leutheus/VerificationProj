from django.contrib import admin

from vericloud.models import Testfile, Benchmark
# Register your models here.
admin.site.register(Testfile)
admin.site.register(Benchmark)