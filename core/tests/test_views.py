# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class IndexViewTestCase(TestCase):

	def seTup(self):
		self.client = Client()
		self.url = reverse('index')


	def tearDown(self):
		pass

	
	# verfica se retorna o http 200
	def test_status_code(self):
		# response = self.client.get(self.url)
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)


	# verfica se está usando o template index.html
	def test_template_used(self):
		# response = self.client.get(self.url)
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'index.html')

class ContactViewTestCase(TestCase):

	def seTUp(self):
		self.client = Client()
		self.url = reverse('contact')
