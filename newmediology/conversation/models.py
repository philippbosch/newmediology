import json
import re
import requests

from django.core.cache import cache
from django.db import models
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _


class AnswerManager(models.Manager):
    def get_by_question(self, question):
        for answer in self.get_query_set().filter(active=True).all():
            regex = answer.get_regex()
            matches = regex.search(question)
            if matches:
                answer.matches = matches.groups()
                return answer
        return None


class Answer(models.Model):
    slug = models.SlugField()
    sample_question = models.CharField(max_length=255, verbose_name=_("sample question"))
    
    trigger_keywords = models.CharField(max_length=255, blank=True, verbose_name=_("keywords"), help_text=_("One or more keywords, separated by commas"))
    trigger_regex = models.CharField(max_length=255, blank=True, verbose_name=_("regular expression"), help_text=_("e.g. '^(hello|hi)' (do not include slashes)"))
    
    action_text = models.TextField(blank=True, verbose_name=_("text"), help_text=_("Reply with a static text (Markdown-enabled)"))
    action_page = models.URLField(blank=True, verbose_name=_("page"), help_text=_("Show internal page (from GitHub Pages) on the stage, enter URL here."))
    action_url = models.URLField(blank=True, verbose_name=_("URL"), help_text=_("Show arbitrary web page on the stage, enter URL here."))
    action_javascript = models.TextField(blank=True, verbose_name=_("JavaScript"), help_text=_("Execute JavaScript function. Matched groups from regular expression are available as 'm'. Return string (Markdown-enabled)."))
    
    order = models.PositiveIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    objects = AnswerManager()
    
    def __init__(self, *args, **kwargs):
        super(Answer, self).__init__(*args, **kwargs)
        self._meta.get_field_by_name('action_page')[0]._choices = lazy(get_github_pages_choices, list)()
    
    def __unicode__(self):
        return u"%s" % self.slug
    
    def get_regex(self):
        if len(self.trigger_keywords):
            return re.compile(r'(%s)' % "|".join(re.split('\s*,\s*',self.trigger_keywords.strip())))
        return re.compile(self.trigger_regex)
    
    class Meta:
        ordering = ('order',)


def get_github_pages_choices():
    pages_choices = cache.get('github_pages_choices')
    if not pages_choices:
        req = requests.get('http://newmediology.github.com/pages.newmediology.org/pages.json')
        if req.ok:
            pages = json.loads(req.text)
        else:
            pages = []
        pages_choices = [(page['url'], "%s (%s)" % (page['title'], page['url'])) for page in pages]
        cache.set('github_pages_choices', pages_choices, 60)
    return pages_choices
