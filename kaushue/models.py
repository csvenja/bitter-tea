from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=100000)
    reference = models.ManyToManyField("self", symmetrical=False, blank=True)

    def __unicode__(self):
        return self.title


class Connection(models.Model):
    from_question = models.IntegerField()
    to_question = models.IntegerField()
    logic = models.CharField(max_length=100000)

    def __unicode__(self):
        return
