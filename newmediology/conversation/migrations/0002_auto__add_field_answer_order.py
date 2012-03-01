# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Answer.order'
        db.add_column('conversation_answer', 'order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Answer.order'
        db.delete_column('conversation_answer', 'order')


    models = {
        'conversation.answer': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Answer'},
            'action_javascript': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'action_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'trigger_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'trigger_regex': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['conversation']
