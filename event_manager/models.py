from django.db import models
from user_manager.models import User
from .choices import EVENT_CATEGORY_CHOICES
class EventTag(models.Model):
    title = models.CharField(max_length=20)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return '{}'.format(self.title)

class Event(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=1000,null=False,blank=False)
    registration_link = models.CharField(max_length=250,null=False,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_events')
    tags = models.ManyToManyField(EventTag)
    clicks = models.ManyToManyField(User,related_name='clicked_events')
    likes = models.ManyToManyField(User,related_name='liked_events')
    category = models.CharField(max_length=20,choices=EVENT_CATEGORY_CHOICES)
    fees = models.DecimalField(max_digits=7,decimal_places=2)
    sponsored = models.BooleanField(default=False)
    
    def __str__(self):
        return '{}'.format(self.title)
    
