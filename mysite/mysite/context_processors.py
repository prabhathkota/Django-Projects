# -*- coding: utf-8 -*-

#using RequestContext in templates
def custom_proc_outside(request):
    #"A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My custom_proc_outside app - Prabhath',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }