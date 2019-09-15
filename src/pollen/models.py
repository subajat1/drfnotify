from django.contrib.auth.models import Group, User
from django.db import models

from webpush import send_user_notification

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

    class Meta:
        ordering = ['-created']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    def __str__(self):
        return str(self.id)

    def save(self, *args, **kw):
        old = type(self).objects.get(pk=self.pk) if self.pk else None
        super(Message, self).save(*args, **kw)

        if old is None and self.content is not None:
            receivers = User.objects.filter(groups=self.content.receiver)
            if len(receivers) > 0:

                payload = {
                    'head': self.content.head + self.head_data,
                    'body': self.content.body + self.body_data,
                    'icon': self.content.icon,
                    'sound': self.content.sound,
                    'url': self.content.url + self.url_data
                }

                for receiver in receivers:
                    send_user_notification(user=receiver, payload=payload, ttl=1000)
        