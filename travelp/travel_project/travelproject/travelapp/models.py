from django.db import models


# Create your models here.
class Place(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()


class Team(models.Model):
    def __str__(self):
        return self.member
    member = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    about = models.TextField()
