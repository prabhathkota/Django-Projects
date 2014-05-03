# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from mysite.polls.models import Choice, Poll
from django.views import generic

# Create your views here.
def polls_wo_template(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)

def polls_with_template(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def polls_with_render_template(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'index.html', context)


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'detail.html', {
            'poll': p,
            'error_message': "Kindly select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('mysite.polls.views.results', args=(p.id,)))
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
        #return HttpResponseRedirect("/polls/%s/results/" % p.id)
		
# def poll_details(request, poll_id):
    # poll = get_object_or_404(Poll, pk=poll_id)
    # return render(request, 'detail.html', {'poll': poll})

# def poll_results(request, poll_id):
    # poll = get_object_or_404(Poll, pk=poll_id)
    # return render(request, 'results.html', {'poll': poll})


#from django.views import generic
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'results.html'


	
# def detail(request, poll_id):
    # return HttpResponse("You're looking at poll %s." % poll_id)

# def results(request, poll_id):
    # return HttpResponse("You're looking at the results of poll %s." % poll_id)

# def vote(request, poll_id):
    # return HttpResponse("You're voting on poll %s." % poll_id)