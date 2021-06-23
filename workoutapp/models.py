from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.event_name

class Content(models.Model):
    event = models.CharField(max_length=50, default='')
    weight = models.IntegerField(null=True, default=0)
    set_number = models.IntegerField(default=0)
    training_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, default='')

    def __str__(self):
        return str(self.event)
