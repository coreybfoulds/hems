from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
		url(r'^admin/',include(admin.site.urls)),
		url(r'^users/',include('users.urls', namspace='users')),
		url(r'',include('hems_blog.urls',namespace='hems_blog')),

		]
