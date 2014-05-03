# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.http import *
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context, Template
from django.template import RequestContext
from mysite.context_processors import custom_proc_outside
from mysite.contacts.models import Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
import subprocess
from django.http import StreamingHttpResponse
import sys
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import simplejson
import socket


#@login_required(login_url='/accounts/login/')
#@login_required() #Called as decorators

def contacts_login(request):
    logout(request)
    username = password = ''
    errors = []
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('contacts_listing'))
                #return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
            else:
                errors.append("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            errors.append("The username and password were incorrect.")
            
    #return render_to_response('contacts_login.html', context_instance=RequestContext(request))
    return render(request, 'contacts_login.html', {'errors' : errors})
    
#@login_required(login_url='/contacts/login/') 
#We can mention the same in urls.py itself
def contacts_listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 2) # Show 2 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('contacts_list.html', {"contacts": contacts, "no_of_pages": paginator.num_pages})

def load_email(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #context = {'latest_poll_list': latest_poll_list}
    #return render(request, 'index.html', context)
    return render(request, 'send_email.html')
    
from django.core.mail import send_mail, BadHeaderError

def send_email(request):
    errors = []
    if request.POST:
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['prabhathkota@gmail.com'])
            except BadHeaderError:
                #return HttpResponse('Invalid header found')
                errors.append('Invalid header found')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            #return HttpResponse('Make sure all fields are entered and valid')
            errors.append('Make sure all fields are entered and valid')
    return render(request, 'send_email.html', {'errors' : errors})        

def thank_you(request):
    return render(request, 'thank_you.html')
    
def sanity_list_testcases(request):
    sanity_list = ['aaa', 'bbb', 'ccc', 'dddddddddddddddd1', 'eeeeeeee1', 'fff114411111111111111', 'ggg', 'hhh']
    #side_bar = ['Sanity List', 'System List']
    side_bar = {'Sanity List':'sanity_list_testcases', 'System List': 'sanity_list_testcases'}
    return render(request, 'sanity_list_testcases.html', {'sanity_testcase_names' : sanity_list, 'side_bar' : side_bar})

def home_view(request):
    center_content = right_side_bar = left_side_bar = ['Home', 'Array', 'List', 'Dict', 'RegExp', 'Count', 'List Comprehension', 'Thread', 'Test']
    #side_bar = {'Sanity List':'sanity_list_testcases', 'System List': 'sanity_list_testcases'}
    #return render(request, 'mysite_home.html', {'sanity_testcase_names' : sanity_list, 'side_bar' : side_bar})
    return render(request, 'mysite_home.html', {'left_side_bar' : left_side_bar, 'right_side_bar' : right_side_bar, 'center_content' : center_content})
    
def stream_response_generator():
    command = 'python C:\\Prabhath\\django_workspace\\mysite\\mysite\\contacts\\test.py'
    for line in run_command(command):
        var = 'Line from browser is : ' + line
        yield var

def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

def run_testcase(request):
    stream_response = selected_tests = []
    side_bar = {'Sanity List':'sanity_list_testcases', 'System List': 'sanity_list_testcases'}
    if request.POST:
        selected_tests = request.POST.getlist('testcases')
        stream_response = StreamingHttpResponse(stream_response_generator())
        return render(request, 'sanity_results.html', {'my_stream_data': stream_response, 'selected_tests': selected_tests, 'side_bar' : side_bar})
    else:
        return HttpResponseRedirect(reverse('sanity_list_testcases'))

def test_template_inheritance(request):
    arr = ['aaa', 'bbb', 'ccc', 'dddddddddddddddddddd', 'eeeeeeeeeeeeeeeeeeee', 'fff', 'ggg', 'hhh']
    side_bar = ['Home', 'List Sanity', 'List System']
    return render(request, 'frontpage.html', {'arr' : arr, 'side_bar' : side_bar})

    
#--------------------------------- Ajax Examples ---------------------------
def ajax_home(request):
    return render(request, 'ajax_home.html')

def ajax_process(request):
   if request.POST.has_key('client_response'):
        x = request.POST['client_response']                  
        y = socket.gethostbyname(x)                           
        response_dict = {}                                          
        response_dict.update({'server_response' : y })                                                                   
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript') 
   else:
        return render(request, 'ajax_home.html')
    
#--------------------------------- Dajax Example ---------------------------

#from dajaxice.decorators import dajaxice_register
#Do it later

    
#------------------------------------------
t = Template('{{ my_stream_data }}')

def gen_rendered():
    for x in range(1,15000):
        c = Context({'my_stream_data': x})
        yield t.render(c)

def stream_view(request):
    response = StreamingHttpResponse(gen_rendered())
    #return response
    return render(request, 'a.html', {'my_stream_data': response})
#------------------------------------------
import json

def return_json(request):
    # Create the HttpResponse object with the appropriate CSV header.
    #response = HttpResponse(content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="test.csv"'

    response_data = [{
        "from": "Steve Jobs",
        "subject": "I think I'm holding my phone wrong :/",
        "sent": "2013-10-01T08:05:59Z"
    },{
        "from": "Ellie Goulding",
        "subject": "I've got Starry Eyes, lulz",
        "sent": "2013-09-21T19:45:00Z"
    },{
        "from": "Michael Stipe",
        "subject": "Everybody hurts, sometimes.",
        "sent": "2013-09-12T11:38:30Z"
    },{
        "from": "Jeremy Clarkson",
        "subject": "Think I've found the best car... In the world",
        "sent": "2013-09-03T13:15:11Z"
    }];
   
    response = json.dumps(response_data)
 
    return HttpResponse(response, content_type="application/json; charset=utf-8")
    #return HttpResponse(json.dumps(response_data))

def return_jsonp(request):
    # Create the HttpResponse object with the appropriate CSV header.
    #response = HttpResponse(content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="test.csv"'

    response_data = [{
        "from": "Steve Jobs",
        "subject": "I think I'm holding my phone wrong",
        "sent": "2013-10-01T08:05:59Z"
    },{
        "from": "Ellie Goulding",
        "subject": "I've got Starry Eyes, lulz",
        "sent": "2013-09-21T19:45:00Z"
    },{
        "from": "Michael Stipe",
        "subject": "Everybody hurts, sometimes.",
        "sent": "2013-09-12T11:38:30Z"
    },{
        "from": "Jeremy Clarkson",
        "subject": "Think I've found the best car... In the world",
        "sent": "2013-09-03T13:15:11Z"
    }];
   
    callback = request.GET.get('callback', '')

    resp = json.dumps(response_data)
    response = callback + '(' + resp + ');'
    #JSON_CALLBACK({"name": "Todd Motto", "id": "80138731"}); 
    
    return HttpResponse(response, content_type="application/json")
    #return HttpResponse(json.dumps(response_data))
