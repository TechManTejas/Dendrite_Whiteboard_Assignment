from django.db import models
from django.contrib.auth.models import User

class Whiteboard(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    clients = models.ManyToManyField(User, related_name='whiteboard_clients', blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='whiteboard_images/', null=True, blank=True)
    data = models.JSONField(default=dict)  # Assuming you want to store JSON data for drawing
    chats = models.TextField(default='')  # Assuming simple text chat for now
    invitees = models.ManyToManyField(User, related_name='whiteboard_invitees', blank=True)

    def __str__(self):
        return self.title
