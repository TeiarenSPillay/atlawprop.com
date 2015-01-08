from django.conf.urls import *
import settings

from eos.urls import urlpatterns as eos_urlpatterns


def direct_to_template(request, template):
    from django.shortcuts import render_to_response
    from django.template import RequestContext
    return render_to_response(template, {'request': request}, context_instance = RequestContext(request))


urlpatterns = patterns('',
    # Static Directories
    (r'^html/(?P<path>.*)$',                      'django.views.static.serve',  {'document_root': settings.TEMPLATE_DIRS[0]}),
    (r'^assets/(?P<path>.*)$',                    'django.views.static.serve',  {'document_root': settings.MEDIA_ROOT}),
    (r'^jsi18n/$',                                'django.views.i18n.javascript_catalog', {'packages': 'django.conf'}),
    
    # Property Search
    (r'^bookmark-share/$',                        'urls.direct_to_template', {'template': 'property-search/includes/bookmark-share.html'}),
    (r'^rss-feed/$',                              'urls.direct_to_template', {'template': 'property-search/includes/rss-feed.xml'}),
    (r'^email/results/$',                         'urls.direct_to_template', {'template': 'emails/results.html'}),
    
    # News
    (r'^advice/$',                                'urls.direct_to_template', {'template': 'news/general-advice.html'}),
    (r'^email/news-details/$',                    'urls.direct_to_template', {'template': 'emails/news-details.html'}),
    (r'^email/newsletter/$',                      'urls.direct_to_template', {'template': 'emails/newsletter.html'}),
    (r'^pdf-test/$',                      'urls.direct_to_template', {'template': 'pdftest.html'}),
)

urlpatterns += eos_urlpatterns
