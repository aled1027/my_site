from django.conf.urls import *
from school.views import *

urlpatterns = patterns('',

	url(r'^$', course_list, name="school_course_list"),
	url(r'^course/(?P<c_id>\d+)/$', course_detail, name="school_course_detail"),
	url(r'^course/(?P<c_id>\d+)/form/$', course_form, name="school_course_form"),
	url(r'^course/form/$', course_form, name="school_course_form"),
	url(r'^course/(?P<c_id>\d+)/delete/$', course_delete, name="school_course_delete"),

	url(r'^course/(?P<c_id>\d+)/homework/(?P<h_id>\d+)/$', homework_detail, name="school_homework_detail"),
	url(r'^course/(?P<c_id>\d+)/homework/form/$', homework_form, name="school_homework_form"),
	url(r'^course/(?P<c_id>\d+)/homework/(?P<h_id>\d+)/form/$', homework_form, name="school_homework_form"),
	url(r'^course/(?P<c_id>\d+)/homework/(?P<h_id>\d+)/delete/$', homework_delete, name="school_homework_delete"),

	url(r'^course/(?P<c_id>\d+)/homework/(?P<h_id>\d+)/program/form/$', program_form, name="school_program_form"),
	url(r'^course/(?P<c_id>\d+)/homework/(?P<h_id>\d+)/program/(?P<p_id>\d+)/$', program_detail, name="school_program_detail"),

	url(r'^upload/$', upload_file, name="school_upload_file"),
)

