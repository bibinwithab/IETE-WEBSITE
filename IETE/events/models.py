from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    # time = models.TimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField()
    # image = models.ImageField(upload_to='events/images/',default='')

    def __str__(self):
        return self.name
    

