from django.db import models
from django.contrib import admin

from datetime import datetime

class Course(models.Model):
	name = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	# other fields: meeting times, blog post with comments, grades
	# graphs
	def __unicode__(self):
		return self.name

class Homework(models.Model):
	course = models.ForeignKey(Course, related_name="homeworks")
	name = models.CharField(max_length=60)
	file_field = models.FileField(upload_to='documents/', blank=True)
	due_date = models.DateTimeField(blank=True, default=datetime.now())
	points = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return u'%s' % self.name

class Program(models.Model):
	homework = models.ForeignKey(Homework, null=True)
	name = models.CharField(max_length=60)
	code = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.name

	def __unicode__(self):
		return self.name


class CourseAdmin(admin.ModelAdmin):
	search_fields=['name']
class HomeworkAdmin(admin.ModelAdmin):
	search_fields=['name']
class ProgramAdmin(admin.ModelAdmin):
	search_fields=['name']

admin.site.register(Course, CourseAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Program, ProgramAdmin)
