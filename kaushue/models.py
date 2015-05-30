from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    reference = models.ManyToManyField(
        "self", through="Connection", symmetrical=False, blank=True)

    def __unicode__(self):
        return self.title


class Connection(models.Model):
    from_question = models.ForeignKey(Question, related_name="from_question")
    to_question = models.ForeignKey(Question, related_name="to_question")
    logic = models.CharField(max_length=1000, blank=True)
