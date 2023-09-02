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
    
class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    college = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

