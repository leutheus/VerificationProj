from django.db import models

# Create your models here.
class Testfile(models.Model):
    CHOICES = (
        ('SAFE', 'SAFE'),
        ('UNSAFE', 'UNSAFE'),
    )
    sha1 = models.CharField(max_length=100,  primary_key=True)
    filename = models.CharField(max_length=255)
    filesize = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_tested = models.DateTimeField(auto_now=True)
    expected_result = models.CharField(max_length=20, choices = CHOICES)
    tested_result = models.CharField(max_length=20, choices = CHOICES)
    binary = models.FileField(upload_to ='testfiles')    


    def __unicode__(self):
            return self.filename

class Benchmark(models.Model):
    run = models.ForeignKey(Testfile)
    user = models.CharField(max_length=255)
    duration = models.IntegerField(default=0)
    name = models.CharField(max_length=100)    
    def __unicode__(self):
        return self.user