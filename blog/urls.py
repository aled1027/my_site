from django.conf.urls import patterns, url
from blog.models import *

urlpatterns = patterns('',
	url(r"", "blog.views.main", name="blog_home"),
	url(r"^(\d+)/$", "blog.views.post", name="blog_post"), # is this the detail view of a post?
	url(r"^add_comment/(\d+)/$", "blog.views.add_comment", name="blog_add_comment"),
	url(r"^delete_comment/(\d+)/$", "blog.views.delete_comment", name="blog_delete_comment"),
	url(r"^delete_comment/(\d+)/(\d+)/$", "blog.views.delete_comment", name="blog_delete_comment_2"),
	url(r"^month/(\d+)/(\d+)/$", "blog.views.month", name="blog_month"),

	# Delete these later
	url(r"", "blog.views.main", name="home"),
)
