from django.db import models

#Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name
    
class Comment(models.Model):
    topic=models.ForeignKey('Topic',on_delete=models.DO_NOTHING)
    name= models.CharField(max_length=264)
    def __str__(self):
        return self.name