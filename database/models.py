from django.db import models

# Create your models here.

class Benchmark(models.Model):
	user = models.CharField(max_length=255)
	def __unicode__(self):
		return self.user


class Run(models.Model):
	revision = models.IntegerField(default=0)

class File(models.Model):
	inBenchmark = models.ForeignKey(Benchmark)
	filename = models.CharField(max_length=255)
	filesize = models.IntegerField(default=0)
	date_added = models.DateTimeField('date added')
	date_tested = models.DateTimeField('date of last test')
	expected_result = models.CharField(max_length=255)
	tested_result = models.CharField(max_length=255)
	binary = models.FileField(db_index = True, upload_to ='testfiles')

class Configuration(models.Model):
	timelimit = models.IntegerField(default=0)
