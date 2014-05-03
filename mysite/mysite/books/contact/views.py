# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from mysite.books.models import Book
from mysite.books.contact.forms import ContactForm
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template.loader import get_template

from django.shortcuts import get_object_or_404

#from django.views.generic import list_detail #Deprecated
from django.views.generic.list import ListView

from mysite.books.models import Book, Publisher


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
                # cd['subject'],
                # cd['message'],
                # cd.get('email', 'noreply@example.com'),
                # ['siteowner@example.com'],
            # )
            #url = reverse('thank_you', {'classname':'contacts'})
            #return HttpResponseRedirect(url)
            return HttpResponseRedirect('/contact/thank_you/')
            #return render(request, 'thank_you.html', {'classname': 'contacts',})
    else:
        form = ContactForm(
            initial={'subject': 'I love your site1112!'}
        )
    return render(request, 'contact_form.html', {'form': form})

def thank_you(request):
    #return render(request, 'thank_you.html')
	return render(request, 'thank_you.html')
	
def books_by_publisher(request, name):
    # Look up the publisher (and raise a 404 if it can't be found).
    publisher = get_object_or_404(Publisher, name__iexact=name)
    
    #(r'^publishers/$', list_detail.object_list, publisher_info), #Deprecated
    #url(r'^publishers/Apress/$', ListView.as_view(queryset = Publisher.objects.filter(name='Apress'), template_name = 'publisher_list_page.html')),
	
    # Use the object_list view for the heavy lifting.
    # return list_detail.object_list(
        # request,
        # queryset = Book.objects.filter(publisher=publisher),
        # template_name = 'books/books_by_publisher.html',
        # template_object_name = 'book',
        # extra_context = {'publisher': publisher}
    # )
    return( ListView.as_view(queryset = Book.objects.filter(publisher=publisher), template_name = 'books_by_publisher.html', template_object_name = 'book') )