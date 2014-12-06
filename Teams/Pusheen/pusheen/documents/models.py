from django.db import models

# Create your models here.
class Title(models.Model):
    titleText = models.TextField()

class SubTitle(models.Model):
    subTitleText = models.TextField()
    titleID = models.ForeignKey(Title)

class Content(models.Model):
    content = models.TextField()
    subTitleID = models.ForeignKey(SubTitle)

class Keyword(models.Model):
    startPos = models.IntegerField()
    length = models.IntegerField(default=1)
    contentID = models.ForeignKey(Content)

