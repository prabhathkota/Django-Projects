from tastypie.authorization import Authorization 
from tastypie.resources import ModelResource
from mysite.books.models import Author, Publisher
from mysite.polls.models import Poll, Choice
from django.contrib.auth.models import User
from tastypie import fields

from django.core.serializers import json 
from django.utils import simplejson 
from tastypie.serializers import Serializer

#http://127.0.0.1:8000/api/expose/author/
#http://127.0.0.1:8000/api/expose/author/1/
#http://127.0.0.1:8000/api/expose/author/schema/  *******

class PrettyJSONSerializer(Serializer): 
    json_indent = 4 
 
    def to_json(self, data, options=None): 
        options = options or {} 
        data = self.to_simple(data, options) 
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent) 


class AuthorResource(ModelResource):
    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'
        serializer = PrettyJSONSerializer()
        authorization= Authorization()
        always_return_data = True

    def determine_format(self, request):
        return 'application/json'

#http://127.0.0.1:8000/api/expose/publisher
#http://127.0.0.1:8000/api/expose/publisher?format=json
class PublisherResource(ModelResource):
    class Meta:
        queryset = Publisher.objects.all()
        resource_name = 'publisher'
        serializer = PrettyJSONSerializer()
        authorization= Authorization()
        always_return_data = True

    def determine_format(self, request):
        return 'application/json'


#http://127.0.0.1:8000/api/expose/poll/
class PollResource(ModelResource): 
    choices = fields.ToManyField('mysite.api.ChoiceResource', 'choice_set', related_name='poll', full=True) 

    class Meta: 
        queryset = Poll.objects.all()
        resource_name = 'poll'
        serializer = PrettyJSONSerializer()
        allowed_methods = ['get', 'post', 'put', 'delete']
        
    def determine_format(self, request):
        return 'application/json'
 
class ChoiceResource(ModelResource): 
    poll = fields.ForeignKey('mysite.api.PollResource', 'poll', related_name='choices')
 
    class Meta:
        queryset = Choice.objects.all()
        serializer = PrettyJSONSerializer()

    def determine_format(self, request):
        return 'application/json'

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        serializer = PrettyJSONSerializer()
        allowed_methods = ['get']
        excludes = ['email', 'password', 'is_superuser']

    def determine_format(self, request):
        return 'application/json'

    #Suppose if you wish to include additional data in a response which is not obtained from a field or method on your model. You can easily extend the dehydrate() method to provide additional values
    def dehydrate(self, bundle):
        bundle.data['custom_field'] = "New field added to User"
        return bundle