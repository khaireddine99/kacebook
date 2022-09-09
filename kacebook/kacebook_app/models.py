from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    """a message sent or recieved by a user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reciever = models.CharField(max_length=200)

    def __str__(self):
        """return the message"""
        return self.text
