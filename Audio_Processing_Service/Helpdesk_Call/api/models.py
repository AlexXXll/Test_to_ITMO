from django.db import models
from django.conf import settings
from audiofield.fields import AudioField
import os.path

class AudioMessage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    audio_file = AudioField(upload_to='your/upload/dir', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='AudioMessages', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

def audio_file_player(self):
    """audio player tag for admin"""
    if self.audio_file:
        file_url = settings.MEDIA_URL + str(self.audio_file)
        player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
        return player_string

audio_file_player.allow_tags = True
audio_file_player.short_description = ('Audio file player')