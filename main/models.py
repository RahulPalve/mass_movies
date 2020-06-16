from django.db import models
class Movie(models.Model):
    id=models.CharField(max_length=9, primary_key=True, unique=True)
    title=models.CharField(max_length=30, default='None')
    poster=models.URLField(default='')
    plot=models.TextField(default='')
    dl_link=models.URLField(default='')

    def __str__(self):
        return self.title

# Create your models here.
