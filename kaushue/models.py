from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=100000)
    referenced_page = models.ManyToManyField("self", symmetrical=False, blank=True)

    def __unicode__(self):
        return self.title
