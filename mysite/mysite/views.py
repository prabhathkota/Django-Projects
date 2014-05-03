from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime
from django.template import RequestContext
from mysite.context_processors import custom_proc_outside

def hello(request):
    return HttpResponse("Hello world 1111")
	
def home(request):
    return HttpResponse("This is Home Page 1111")
	
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
	
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

#using normal templates	
#from django.template.loader import get_template
#from django.template import Context
def current_datetime_1(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)	

#using render templates	
#from django.shortcuts import render
#It will fetch the template from TEMPLATE_DIRS defined in settings.py
def current_datetime_2(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def thank_you(request):
    return render(request, 'thank_you.html')

#using RequestContext in templates
def custom_proc(request):
    #"A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app - Prabhath',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

def request_context_local_1(request):
    # Using custom_proc as defined above ie., you can define custom function to pass commonly used parameters to pass to tempalte by default
    return render(request, 'request_context_template.html',
        {'message': 'I am in view 111.'},
        context_instance=RequestContext(request, processors=[custom_proc]))

def request_context_local_2(request):
    # Using Custom Proc ie., you can define custom function to pass commonly used parameters to pass to tempalte by default
    return render(request, 'request_context_template.html',
        {'message': 'I am in view 222.'},
        context_instance=RequestContext(request, processors=[custom_proc]))

#Calling custom_proc_outside which defined in context_processor.py
#This 'context_processor.py' has benn added to TEMPLATE_CONTEXT_PROCESSORS in settings.py, check there
def request_context(request, offset):
    # Using Custom Proc ie., you can define custom function to pass commonly used parameters to pass to tempalte by default
    offset = int(offset)
    message = ''
    if offset == 1:
        message = 'I am in view 1'
    elif offset == 2:
        message = 'I am in view 2'
    else:
        message = 'I am in view %d' % offset
    return render(request, 'request_context_template.html',
        {'message': message},
        context_instance=RequestContext(request, processors=[custom_proc_outside]))		


