from django.db import models

# Create your models here.
class Title(models.Model):
    titleText = models.TextField()
    articleID = models.ForeignKey(Article)
    def __unicode__(self):
        return self.titleText

class SubTitle(models.Model):
    subTitleText = models.TextField()
    titleID = models.ForeignKey(Title)
    isImportant = models.BooleanField(default=False)
    def __unicode__(self):
        return self.subTitleText

class Content(models.Model):
    content = models.TextField()
    subTitleID = models.ForeignKey(SubTitle)
    isImportant = models.BooleanField(default=False)
    def __unicode__(self):
        return self.contentText

class Keyword(models.Model):
    startPos = models.IntegerField()
    length = models.IntegerField(default=1)
    contentID = models.ForeignKey(Content)

