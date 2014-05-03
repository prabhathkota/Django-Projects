#from django.conf.urls import patterns, include, url
from django.conf.urls import *
import mysite.views

#from mysite.books import views
import mysite.books.views
import mysite.books.contact.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', mysite.views.home),
	url(r'^mysite/$', mysite.views.home),
	url(r'^hello/$', mysite.views.hello),
	url(r'^time/$', mysite.views.current_datetime),
	url(r'^template1/$', mysite.views.current_datetime_1),
	url(r'^template2/$', mysite.views.current_datetime_2),
	url(r'^time/plus/(\d{1,2})/$', mysite.views.hours_ahead),

    url(r'^search_form/$', mysite.books.views.search_form),
	url(r'^search/$', mysite.books.views.search),
	url(r'^meta/$', mysite.books.views.display_meta),
	url(r'^search_book/$', mysite.books.views.search_book),
	#url(r'^search_book_results/$', mysite.books.views.search_book_results),
	
	#Contact with out using django forms
	url(r'^contact_wo_form/$', mysite.books.views.contact_wo_form),
	
	#Under Contacs folder in books
	#Contact with using django forms
	url(r'^contact/$', mysite.books.contact.views.contact),
	url(r'^contact/thank_you/$', mysite.books.contact.views.thank_you), 
	
)
