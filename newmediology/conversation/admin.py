from django.contrib import admin

from .models import Answer, UnansweredQuestion


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('slug', 'trigger', 'active', 'order',)
    list_editable = ('active', 'order',)
    fieldsets = (
        (None, {
            'fields': ('slug', 'order', 'active',)
        }),
        ('Trigger', {
            'fields': ('trigger_keywords', 'trigger_regex',),
            'description': '<p class="help">Please choose <strong>one</strong> type of trigger.</p>',
        }),
        ('Action', {
            'fields': ('action_text', 'action_page', 'action_url', 'action_javascript',)
        })
    )
    
    def trigger(self, instance):
        if len(instance.trigger_keywords):
            return u"Keywords: %s" % instance.trigger_keywords
        if len(instance.trigger_regex):
            return u"RegEx: %s" % instance.trigger_regex
    
admin.site.register(Answer, AnswerAdmin)


class UnansweredQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'asked',)
    readonly_fields = ('asked',)

admin.site.register(UnansweredQuestion, UnansweredQuestionAdmin)
