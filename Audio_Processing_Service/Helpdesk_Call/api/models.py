from django.db import models
from django.conf import settings
import os.path

class AudioMessage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    audio_file = models.FileField(upload_to='uploads/')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='AudioMessages', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
