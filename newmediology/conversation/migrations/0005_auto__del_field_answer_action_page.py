# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Answer.action_page'
        db.delete_column('conversation_answer', 'action_page')


    def backwards(self, orm):
        
        # Adding field 'Answer.action_page'
        db.add_column('conversation_answer', 'action_page', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)


    models = {
        'conversation.answer': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Answer'},
            'action_javascript': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sample_question': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'trigger_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'trigger_regex': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['conversation']
