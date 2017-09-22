from django.conf.urls import  url, include
from django.contrib import admin

from core import views
from catalog import views as views_catalog
from django.contrib.auth.views import login, logout


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contato/$', views.contact, name='contact'),
	url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
	url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
	url(r'^registro/$', views.register,  name='register'),
	url(r'^vagas/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls),
]
