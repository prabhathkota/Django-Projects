How to start Django Development Server
#######################################
Django develeopment server works on default port 8000
python manage.py runserver 8000 

Using Django Development Server
########################
http://127.0.0.1:8000/

Using Apache Server (If you configure Apache)
###############################################
http://127.0.0.1/mysite/

How to configure Apache with Django
######################################
In Apache httpd.conf
WSGScriptAlias /mysite "C:/django_workspace/mysite/mysite/wsgi.py"

RESTFul Services Using Tastypie
##################################

Refer api.py and urls.py

e.g.,
from mysite.api import *
from tastypie.api import Api

expose_api = Api(api_name='expose')
expose_api.register(AuthorResource())
expose_api.register(PublisherResource())
expose_api.register(PollResource())
expose_api.register(ChoiceResource())
expose_api.register(UserResource())


http://127.0.0.1:8000/api/expose/author/
http://127.0.0.1:8000/api/expose/author/1/
http://127.0.0.1:8000/api/expose/author/schema/

http://127.0.0.1:8000/api/expose/poll/

http://127.0.0.1:8000/api/expose/publisher
http://127.0.0.1:8000/api/expose/publisher?format=json

Generic Class Based Views
##########################
In urls.py refer 
Generic Views for Polls -> IndexView, DetailView, ResultsView, ListView