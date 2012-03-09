from django.conf import settings
from django.db import models

from markdown import markdown


class Page(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    text_html = models.TextField(editable=settings.DEBUG, blank=True)
    slug = models.SlugField()
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s (%s)" % (self.title, self.slug)
    
    def save(self, *args, **kwargs):
        self.text_html = markdown(self.text, extensions=['extra'])
        super(Page, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('page', [self.slug])