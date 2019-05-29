from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=32)
    Email = models.EmailField()
    Reason = models.CharField(max_length=32)
    Message = models.CharField(max_length=1030)


class Intereste(models.Model):
    Interest = models.CharField(max_length=264)
    Skill = models.CharField(max_length=264)
    Activity = models.CharField(max_length=255)

    def __str__(self):
        return self.Interest
# Create your models here.
