from django.db import models
from django.utils import timezone


# Create your models here.
class canvas(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    last_edit = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200, null=True, blank=True)
    urlimage = models.TextField()
    file = models.CharField(max_length=200)

    def __str__(self):
        return """name = {}\nfile location: {}""".format(self.name, self.file)
