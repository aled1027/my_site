http://concentricsky.com/blog/2014/feb/custom-django-widget

To do:
1. Finish homework section
	- each homwork should have a due data, a way to upload files (maybe multiple files.. like for programming)
	- view/download files
	- due date (can port over from code for post/comment dates - should be easy
	- can add ability to track how finished you are with the homework
		- use http://lightbird.net/dbe/todo_list.html as a template
		- not written in 1.6, so just use it as a basis, not a copy/paste/fix
4. "Admin site" for teacher

What I'm writing:
A website for a me. 

Tests:
	python manage.py dumpdata -e contenttypes  > school/fixtures/school_views_testdata.json 
	python manage.py test school
	python manage.py test school -v 2
		-- for verbose; not sure what the two does. 

