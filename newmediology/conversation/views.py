import json

from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import Answer


class TalkView(TemplateView):
    template_name = "conversation/base.html"
    
    def dispatch(self, request, **kwargs):
        if request.is_ajax():
            answer = Answer.objects.get_by_question(request.GET.get('question'))
            data = {}
            if answer:
                data['text'] = answer.action_text
                data['page'] = answer.action_page
                data['url'] = answer.action_url
                data['javascript'] = answer.action_javascript
                data['matches'] = answer.matches
            
            resp = HttpResponse(json.dumps(data))
            resp['Content-Type'] = 'application/json'
            return resp
        return super(TalkView, self).dispatch(request, **kwargs)