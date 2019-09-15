from django.contrib.auth.models import Group
from django.db import models


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, default='')
    sender = models.CharField(max_length=256, blank=True, default='')
    receiver = models.ForeignKey(Group, related_name='content_receiver', on_delete=models.SET_NULL, null=True, blank=True)
    head = models.CharField(max_length=64, blank=True, default='')
    body = models.CharField(max_length=256, blank=True, default='')
    icon = models.CharField(max_length=256, blank=True, default='')
    sound = models.CharField(max_length=256, blank=True, default='')
    url = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.ForeignKey(Content, related_name='message_content', on_delete=models.SET_NULL, null=True, blank=True)
    head_data = models.CharField(max_length=64, blank=True, default='')
    body_data = models.CharField(max_length=256, blank=True, default='')
    url_data = models.CharField(max_length=256, blank=True, default='')
    head_payload = models.CharField(max_length=64, blank=True, default='')
    body_payload = models.CharField(max_length=256, blank=True, default='')
    url_payload = models.CharField(max_length=256, blank=True, default='')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    def __str__(self):
        return self.id

    def save(self, *args, **kw):
        old = type(self).objects.get(pk=self.pk) if self.pk else None

        if old is None:

            _head = None
            if ',' in self.head_data:
                _head = self.head_data.split(',')[0]
            
            self.head_payload = self.content.head + _head

        super(Message, self).save(*args, **kw)
