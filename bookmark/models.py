from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.


class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    time = models.DateTimeField('Time', null=True, blank=True)
    date = models.DateField('date', default=datetime.datetime.now, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s %s" %(self.title, self.url)
        # return self.title
