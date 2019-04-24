from django.db import models


def get_file_path(instance, filename):
    name = 'FILES/%s/%s-%s' % (
        filename, filename, instance.version
    )
    return name


class FileManager(models.Model):
    file = models.FileField(
        upload_to=get_file_path,
        null=True, default=None, blank=True)
    version = models.CharField(default='', max_length=100)
    file_name = models.CharField(default='', max_length=100)
    description = models.CharField(
        default='', max_length=2000, blank=True)
