from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    needed_permission = models.TextField()

    def __str__(self):
        return self.title


class Session(models.Model):
    title = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/', null=True)
    video_file = models.FileField(upload_to='videos/', null=True)

    def __str__(self):
        return self.title
