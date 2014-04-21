from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Project(models.Model):
    subject = models.CharField(max_length=140)
    text = models.TextField()
    url = models.URLField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.subject