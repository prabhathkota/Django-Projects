# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from mysite.books.models import Book
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template.loader import get_template

from django.http import Http404
from django.template import TemplateDoesNotExist

#from django.views.generic.simple import direct_to_template #Deprecated
from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404

#from django.views.generic import list_detail #Deprecated
from django.views.generic import ListView, DetailView
from mysite.books.models import Book, Publisher

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table border=1>%s</table>' % '\n'.join(html))


def search_book(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            print books
            return render(request, 'search_book_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_book.html', {'errors': errors})


from django.views.generic.base import View

#Observe, this is a class intead of function, thats why Class Based View
class BooksView(View):  
    #this will get from from django.views.generic.base import View
    #tempalte_name is mandatory
    template_name = 'search_book_results.html'
    errors = []

    def get(self, request, *args, **kwargs):
        #template_name = 'search_book_results1.html'
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            print books
            return render(request, self.template_name, {'books': books, 'query': q})

    #return render(request, self.template_name, {'errors': errors})

#ListView - If U want to print model data
class BooksListView(ListView):
    model = Book
    template_name = "BooksListView.html"
    queryset = Book.objects.all().order_by('-title') #-title prints in desc order, without that, asc order
    context_object_name = 'books_filter_by_name' #This books_filter_by_name is used template to render

#DeatilView - If U want to print model data and additional data
#By default the generic DetailView expects you to provide a pk or slug in the URL as mentioned below
#url(r'^(?P<pk>\d+)/$', view='detail'), 
#If its missing you will get a lovely little error:
class BooksDetailView(DetailView):
    model = Book
    template_name = "BooksDetailView.html"
    #queryset = Book.objects.all().order_by('-title') #-title prints in desc order, without that, asc order
    #context_object_name = 'books_123' #This books_filter_by_name is used template to render

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return self.model.objects.filter(title__icontains=pk)	
	
    #get additional information in that template
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['extra'] = { 'a' : 10, 'b' : 20, 'c' : 30 }
        return context

from mysite.books.contact.forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/thank_you/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super(ContactView, self).form_valid(form)

#Contact without using django forms
def contact_wo_form(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            # send_mail(
                # request.POST['subject'],
                # request.POST['message'],
                # request.POST.get('email', 'noreply@example.com'),
                # ['siteowner@example.com'],
            # )
            #url = reverse('/mysite/thank_you/', {'classname':'books'})
            #return HttpResponseRedirect(url)
            return HttpResponseRedirect('/thank_you/')
            #return render(request, 'thank_you.html', {'classname': 'books',})
    return render(request, 'contact_wo_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })

# def book_thank_you(request):
    # return render(request, 'book_thank_you.html')


#Generic Views    
#from django.http import Http404
#from django.template import TemplateDoesNotExist
#from django.views.generic.simple import direct_to_template
#(r'^about/(\w+)/$', TemplateView.as_view(template_name="about/books.html")),

def about_pages(request, page):
    try:
        #return direct_to_template(request, template="about/%s.html" % page) #Deprecated
        return TemplateView.as_view(template_name="about/books.html")
    except TemplateDoesNotExist:
        raise Http404()

# def books_by_publisher(ListView):
    # Look up the publisher (and raise a 404 if it can't be found).
    #publisher = get_object_or_404(Publisher, name__iexact=name)
    
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
    #return( ListView.as_view(queryset = Book.objects.filter(publisher=publisher), template_name = 'books_by_publisher.html',) )
    # context_object_name = "book_list"
    # template_name = "books_by_publisher.html"

    # def get_queryset(self):
        # publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
        # return Book.objects.filter(publisher=publisher)