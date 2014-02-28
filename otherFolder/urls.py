from django.conf.urls.defaults import *
from my_site.blog.models import *

urlpatterns = patterns('dbe.blog.views',
   (r"^(\d+)/$", "post"),
   (r"^add_comment/(\d+)/$", "add_comment"),
   (r"^delete_comment/(\d+)/$", "delete_comment"),
   (r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
   (r"^month/(\d+)/(\d+)/$", "month"),
   (r"", "main"),
)
