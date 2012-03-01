# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Answer'
        db.create_table('conversation_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('trigger_keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('trigger_regex', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('action_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('action_page', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('action_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('action_javascript', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('conversation', ['Answer'])


    def backwards(self, orm):
        
        # Deleting model 'Answer'
        db.delete_table('conversation_answer')


    models = {
        'conversation.answer': {
            'Meta': {'object_name': 'Answer'},
            'action_javascript': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'action_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'trigger_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'trigger_regex': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['conversation']
