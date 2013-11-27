from django.db import models

# Create your models here.
class Testfile(models.Model):
        filename = models.CharField(max_length=255)
        filesize = models.IntegerField(default=0)
        date_added = models.DateTimeField('date added')
        date_tested = models.DateTimeField('date of last test')
        expected_result = models.CharField(max_length=255)
        tested_result = models.CharField(max_length=255)
        binary = models.FileField(db_index = True, upload_to ='testfiles')

        def __unicode__(self):
                return self.filename

class Benchmark(models.Model):
    run = models.ForeignKey(Testfile)
    user = models.CharField(max_length=255)
    duration = models.IntegerField(default=0)
    name = models.CharField(max_length=100)    
    def __unicode__(self):
        return self.user