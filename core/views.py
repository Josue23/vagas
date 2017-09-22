# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy


User = get_user_model()


def index(request):
	return render(request, 'index.html')


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
	else:
		form = ContactForm()
 	# request.POST
	context = {
		'form': form
	}
	return render(request, 'contact.html', context)


class RgisterView(CreateView):

	form_class = UserCreationForm
	template_name = 'register.html'
	model = User
	success_url = reverse_lazy('login')

register = RgisterView.as_view()