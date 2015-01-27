# coding: utf-8
"""
Definition of urls for xbcWeb.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from app.view.sitemaps import StaticViewSitemap

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

# for sitemap
from django.contrib.sitemaps.views import sitemap

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='index'),
    url(r'^home$', 'app.views.home', name='home'),
    #url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^products$', 'app.views.products', name = 'products'),
    url(r'^delivery_intro$', 'app.views.delivery_intro', name = 'delivery_intro'),
    url(r'^touch$', 'app.views.touch', name = 'touch'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


sitemaps = {
    'static':StaticViewSitemap,
}

urlpatterns += (
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    )
