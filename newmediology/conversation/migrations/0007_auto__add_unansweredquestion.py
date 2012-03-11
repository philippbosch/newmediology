# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UnansweredQuestion'
        db.create_table('conversation_unansweredquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('asked', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('conversation', ['UnansweredQuestion'])


    def backwards(self, orm):
        
        # Deleting model 'UnansweredQuestion'
        db.delete_table('conversation_unansweredquestion')


    models = {
        'conversation.answer': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Answer'},
            'action_javascript': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']", 'null': 'True', 'blank': 'True'}),
            'action_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sample_question': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'trigger_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'trigger_regex': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'conversation.unansweredquestion': {
            'Meta': {'ordering': "('-asked',)", 'object_name': 'UnansweredQuestion'},
            'asked': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {})
        },
        'pages.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['conversation']
