# -*- coding: utf-8 -*-
#from django.conf.urls import patterns, include, url

#from django.conf.urls import *
#import mysite.views
#import mysite.books.views
#import mysite.books.contact.views

#from django.conf.urls.defaults import *  #deprecated
from django.conf.urls import *
from django.conf import settings
from django.views.generic import TemplateView

#from django.views.generic import list_detail #Deprecated
from django.views.generic.list import ListView

from mysite.books.models import Publisher
#from mysite.books.views import books_by_publisher
#from mysite.polls.views import *

from mysite.polls import views
#import django.contrib.auth.views.login
from django.contrib.auth.decorators import login_required

#Contacts
#from mysite.contacts.views import contacts_listing

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
    #url(r'^polls/', include('polls.urls')),
    #url(r'^polls/', include('mysite.polls.urls', namespace="polls")),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^envelope/', include('envelope.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #url(r'^accounts/profile/$', 'django.contrib.auth.views.profile'),
)

urlpatterns += patterns('mysite.views',
	#url(r'^$', 'home'),
	url(r'^mysite/$', 'home'),
	url(r'^hello/$', 'hello'),
	url(r'^time/$', 'current_datetime'),
	url(r'^template1/$', 'current_datetime_1'),
	url(r'^template2/$', 'current_datetime_2'),
	url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    url(r'^thank_you/$', 'thank_you'),
    url(r'^request_context_local_1/', 'request_context_local_1'), #How to read local context processors defined inside views.py
    url(r'^request_context_local_2/', 'request_context_local_2'), #How to read local context processors defined inside views.py
    url(r'^request_context_(\d)/$', 'request_context'), #How to read outside context processors and capture strings in URL's
)

urlpatterns += patterns('mysite.books.views',
    url(r'^search_form/$', 'search_form'),
	url(r'^search/$', 'search'),
	url(r'^meta/$', 'display_meta'),
	url(r'^search_book/$', 'search_book'),
	#url(r'^search_book_results/$', mysite.books.views.search_book_results),

    #Contact with out using django forms
    url(r'^contact_wo_form/$', 'contact_wo_form'),
    #url(r'^book/thank_you/$', 'book_thank_you'),
    #url(r'^about/(\w+)/$', 'about_pages'),
    url(r'^about/(\w+)/$', TemplateView.as_view(template_name="about/books.html")),
    #url(r'^books/(\w+)/$', books_by_publisher.as_view()),
)

from mysite.books.views import BooksView, BooksListView, BooksDetailView, ContactView

urlpatterns += patterns('',
    #---------------- Start Generic Views --------
    url(r'^books/View/$', BooksView.as_view()), #BooksView is a class instead of function
    url(r'^books/ListView/$', BooksListView.as_view()), #BooksListView is a class instead of function    
    url(r'^books/DetailView/(?P<pk>\d+)/$', BooksDetailView.as_view()), #BooksDetailView is a class instead of function
    url(r'^books/ContactView/$', ContactView.as_view()), #ContactView is a class instead of function

	#---------------- End Generic Views ----------
)

#--------------------------------------------- START of POLLS ------------------------------------------------

#mysite.polls.views
urlpatterns += patterns('mysite.polls.views',
    # url(r'^polls_wo_template/$', 'polls_wo_template', name='polls_wo_template'),
    # url(r'^polls_with_template/$', 'polls_with_template', name='polls_with_template'),
    url(r'^polls_with_render_template/$', 'polls_with_render_template', name='polls_with_render_template'),
    # url(r'^polls/(?P<poll_id>\d+)/details/$', 'poll_details', name='poll_details'),
	# url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote', name='vote'),
    # url(r'^polls/(?P<poll_id>\d+)/results/$', 'poll_results', name='poll_results'),
)

#Generic Views for Polls
urlpatterns += patterns('',
    url(r'^polls/$', views.IndexView.as_view(), name='index'),
    url(r'^polls/(?P<pk>\d+)/details/$', views.DetailView.as_view(), name='poll_details'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^polls/(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='poll_results'),
)

#--------------------------------------------- END of POLLS ------------------------------------------------

#--------------------------------------------- START of Contacts ------------------------------------------------

from mysite.contacts.views import contacts_listing, contacts_login, load_email, send_email, thank_you, sanity_list_testcases
from mysite.contacts.views import run_testcase, stream_view, test_template_inheritance, ajax_home, ajax_process

#mysite.polls.views
urlpatterns += patterns('',
    #url(r'^contacts/listing/$', 'contacts_listing', name='contacts_listing'),
    url(r'^contacts/listing/$', login_required(contacts_listing, login_url='/contacts/login/'), name='contacts_listing'),
	url(r'^contacts/login/$', contacts_login, name='contacts_login'),
	url(r'^contacts/load_email/$', load_email, name='contacts_load_email'),
	url(r'^contacts/send_email/$', send_email, name='contacts_send_email'),
	url(r'^contacts/thank_you/$', thank_you, name='contacts_thank_you'),	
    url(r'^sanity/list/$', sanity_list_testcases, name='sanity_list_testcases'),
    url(r'^sanity/run/$', run_testcase, name='run_testcase'),
    url(r'^sanity/stream/$', stream_view, name='stream_view'),
    url(r'^test_ti/$', test_template_inheritance, name='test_template_inheritance'),

    #Ajax
    url(r'^ajax/home/$', ajax_home, name='ajax_home'),
    url(r'^ajax/process/$', ajax_process, name='ajax_process'),
   
)

#--------------------------------------------- END of Contacts ------------------------------------------------



#-------------------------------------------- MySite ----------------------------------------------------------
# from mysite.contacts.views import home_view
# urlpatterns += patterns('',
	# url(r'^home/$', home_view, name='home_view'),

# )
#-------------------------------------------- END of MySite ------------------------------------------------

#--------------------------------------------- START of Tastypie (RESTful API)  ------------------------------------------------

#Ref: http://django-tastypie.readthedocs.org/

#TastyPie Configuring URL
#from mysite.api import AuthorResource, PublisherResource, PollResource, ChoiceResource, UserResource
from mysite.api import *
from tastypie.api import Api

expose_api = Api(api_name='expose')
expose_api.register(AuthorResource())
expose_api.register(PublisherResource())
expose_api.register(PollResource())
expose_api.register(ChoiceResource())
expose_api.register(UserResource())

#E.g., 
#http://127.0.0.1:8000/api/expose/  #This gives the available apis like author, poll, user etc
#http://127.0.0.1:8000/api/expose/author/  #default gives 20 items for pagenation, ?limit=0
#http://127.0.0.1:8000/api/expose/author/?limit=0  #to avoid this pagenation, it gives around limit of 1000 records
#http://127.0.0.1:8000/api/expose/author/schema/  #This gives schema details of author
#http://127.0.0.1:8000/api/expose/author/set/1;3/ #It will give subset of data, it gets 1, 3 records
#http://127.0.0.1:8000/api/expose/author/1/
#http://127.0.0.1:8000/api/expose/poll/1/
#http://127.0.0.1:8000/api/expose/user/1/
urlpatterns += patterns('',
    url(r'^api/', include(expose_api.urls)),
)

from mysite.contacts.views import return_json,return_jsonp

urlpatterns += patterns('',
    url(r'^api/json/$', return_json, name='return_json'),
    url(r'^api/jsonp/$', return_jsonp, name='return_jsonp'),   
)

# #--------------------------------------------- END of Tastypie (RESTful API) -----------------------------------------------

# urlpatterns += patterns('mysite.books.contact.views',	
	# #Under Contacs folder in books
	# #Contact with using django forms
	# url(r'^contact/$', 'contact'),
	# url(r'^contact/thank_you/$', 'thank_you'), 
# )

# #Generic Views of Objects
# publisher_info = {
    # 'queryset': Publisher.objects.all(),
    # 'template_name': 'publisher_list_page.html',
# }

urlpatterns += patterns('',
    #(r'^publishers/$', list_detail.object_list, publisher_info), #Deprecated
    #(r'^publishers/$', ListView.as_view(queryset = Publisher.objects.all(), template_name = 'publisher_list_page.html')),
    (r'^publishers/Apress/$', ListView.as_view(queryset = Publisher.objects.filter(name='Apress'), template_name = 'publisher_list_page.html')),
    (r'^publishers123/$', ListView.as_view(model = Publisher, template_name = 'publisher_list_page.html')),
	#(r'^books/(\w+)/$', books_by_publisher.as_view()),
)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^debuginfo/$', views.debug),
#    )

#If you intend your code to be used on multiple Django-based sites, you should consider arranging your URLconfs in such a way that allows for “including.”
#an include() do not have a $ (end-of-string match character) but do include a trailing slash. 
#Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

#urlpatterns = patterns('',
#    (r'^weblog/', include('mysite.blog.urls')),
#    (r'^photos/', include('mysite.photos.urls')),
#    (r'^about/$', 'mysite.views.about'),
#)