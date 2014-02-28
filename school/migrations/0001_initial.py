# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'school_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'school', ['Course'])

        # Adding model 'Homework'
        db.create_table(u'school_homework', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cl', to=orm['school.Course'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('file_field', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 27, 0, 0), blank=True)),
            ('points', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'school', ['Homework'])

        # Adding model 'Program'
        db.create_table(u'school_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Course'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'school', ['Program'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'school_course')

        # Deleting model 'Homework'
        db.delete_table(u'school_homework')

        # Deleting model 'Program'
        db.delete_table(u'school_program')


    models = {
        u'school.course': {
            'Meta': {'object_name': 'Course'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'school.homework': {
            'Meta': {'object_name': 'Homework'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cl'", 'to': u"orm['school.Course']"}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 27, 0, 0)', 'blank': 'True'}),
            'file_field': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'school.program': {
            'Meta': {'object_name': 'Program'},
            'code': ('django.db.models.fields.TextField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.Course']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['school']