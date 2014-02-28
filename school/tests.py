from django.test import TestCase
from django.core.urlresolvers import reverse
from school.models import *

class SimpleTestCase(TestCase):
	def test_basic_addition(self):
		self.assertEqual(1+1,2)

class SchoolViewTestCase(TestCase):
	fixtures = ['school_views_testdata.json',]

	def test_home(self):
		resp = self.client.get('/school/')
		self.assertEqual(resp.status_code, 200)

	def test_class_detail(self):

		resp = self.client.get('/school/class/1/')
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('class' in resp.context)

		c = resp.context['class']

		self.assertEqual(c.name, "Algorithms")
		self.assertEqual(c.body, "body of algorithms")

		resp  = self.client.get('/school/class/4/')
		self.assertEqual(resp.status_code, 404)

	def test_good_class_form(self):
		resp = self.client.post(reverse("school_class_form"), {'name': 'cname', 'body': 'body of c'}, follow=False)
		self.assertEqual(resp.status_code, 302)

		resp = self.client.post('/school/class/form/', {'name': 'cname', 'body': 'body of c'}, follow=True)
		self.assertEqual(resp.status_code, 200)

		classes = Class.objects.all()
		new_class = classes[len(classes)-1]
		self.assertEqual(new_class.name, 'cname')
		self.assertEqual(new_class.body, 'body of c')

	def test_bad_class_form(self):
		# no name
		resp = self.client.post(reverse("school_class_form"), {'name': '', 'body': 'body of c'}, follow=False)
		self.assertEqual(resp.status_code, 200)
		self.assertFormError(resp, 'form', 'name', 'This field is required.')
		# no body
		resp = self.client.post(reverse("school_class_form"), {'name': 'cname', 'body': ''}, follow=False)
		self.assertEqual(resp.status_code, 200)
		self.assertFormError(resp, 'form', 'body', 'This field is required.')


# form






"""
response = client.get(reverse('blog_detail', args=[2008, 'apr', 2, 'where']))
"""
