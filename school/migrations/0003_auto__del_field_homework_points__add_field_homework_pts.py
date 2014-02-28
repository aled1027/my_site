# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Homework.points'
        db.delete_column(u'school_homework', 'points')

        # Adding field 'Homework.pts'
        db.add_column(u'school_homework', 'pts',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Homework.points'
        db.add_column(u'school_homework', 'points',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Homework.pts'
        db.delete_column(u'school_homework', 'pts')


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
            'newField': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'pts': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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