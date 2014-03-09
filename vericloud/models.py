from django.db import models
# Create your models here.


class File(models.Model):
    hash = models.CharField(max_length=40)
    path = models.CharField(max_length=255)
    file_content = models.FileField(upload_to='testfiles/')

    def __unicode__(self):
        return self.hash + ' ' + self.path

    class Meta:
        db_table = 'file'


class FileHierarchy(models.Model):
    file = models.ForeignKey('File')
    parent = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.parent)

    class Meta:
        db_table = 'file_hierarchy'
        verbose_name_plural = 'FileHierarchies'
        unique_together = ("file", "parent")
        index_together = [["file", "parent"],]

class Limitation(models.Model):
    time_limit = models.IntegerField(default=0)
    memory_limit = models.IntegerField(default=0)
    processor_limit = models.IntegerField(default=0)

    def __unicode__(self):
        result = 'Time: ' + str(self.time_limit)
        result += ' Mem: ' + str(self.memory_limit)
        result += ' CPU: ' + str(self.processor_limit)
        return result

    class Meta:
        db_table = 'limitations'


class Requirement(models.Model):
    processor_count = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    processor_type = models.CharField(max_length=255)

    def __unicode__(self):
        result = 'Processors: ' + str(self.processor_count)
        result += ' Mem: ' + str(self.memory)
        result += ' Processor Type: ' + str(self.processor_type)
        return result

    class Meta:
        db_table = 'requirements'


class VerificationRun(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    realized_task = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    priority = models.TextField()
    output_file_pattern = models.TextField()
    command = models.TextField()
    working_dir = models.CharField(max_length=255)
    requirements = models.ForeignKey('Requirement')
    limitations = models.ForeignKey('Limitation')
    user = models.TextField()

    def __unicode__(self):
        return self.user + ' ' + self.command

    class Meta:
        db_table = 'verification_run'


class VerificationResult(models.Model):
    run = models.ForeignKey('VerificationRun')
    files = models.ForeignKey('FileHierarchy')
    std_out = models.TextField()
    std_err = models.TextField()
    timestamp_of_completion = models.DateTimeField(auto_now_add=True)
    verdict = models.CharField(max_length=50)
    max_memory = models.IntegerField()
    host_information = models.TextField()
    wall_time = models.CharField(max_length=255)

    def __unicode__(self):
        return str(self.timestamp_of_completion)

    class Meta:
        db_table = 'verification_result'