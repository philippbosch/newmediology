import json
from time import sleep

from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import Answer, UnansweredQuestion


class TalkView(TemplateView):
    template_name = "conversation/base.html"
    
    def dispatch(self, request, **kwargs):
        if request.is_ajax() or request.GET.get('ajax', False):
            sleep(.5)
            answer = Answer.objects.get_by_question(request.GET.get('question'))
            data = {}
            if answer:
                data['text'] = answer.action_text or None
                data['page'] = answer.action_page and answer.action_page.get_absolute_url()
                data['url'] = answer.action_url or None
                data['javascript'] = answer.action_javascript or None
                data['matches'] = answer.matches
                data['slug'] = answer.slug
                data['sample_question'] = answer.sample_question
                if answer.slug == 'catch-all':
                    UnansweredQuestion.objects.create(question=request.GET.get('question'))
            
            resp = HttpResponse(json.dumps(data))
            resp['Content-Type'] = 'application/json'
            return resp
        return super(TalkView, self).dispatch(request, **kwargs)