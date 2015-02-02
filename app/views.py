#   coding: utf-8
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.models import ProductCategory
from django.contrib.sitemaps import Sitemap
from django.utils.translation import ugettext as _

import logging
logger = logging.getLogger (__name__)

def prepare_general_cxt ():
    context = {}

    context['year'] = datetime.now().year

    # Translators: The brand name of the site
    context['mybrand'] = _('Xiao Bin Cheng Store')

    all_product_category = ProductCategory.objects.all ()
    context['product_categories'] = all_product_category

    return context

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    context = prepare_general_cxt ()
    context['title'] = _('Home')

    return render(
        request,
        'app/index.html',
        context
    )

#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)

#    context = prepare_general_cxt ()
#    context['title'] = 'Contact'
#    context['message'] = 'Your contact page.'

#    return render(
#        request,
#        'app/contact.html',
#        context
#    )

def touch (request):
    return HttpResponse('Ouch!')


def delivery_intro (request):
    """Renders the delivery_intro page."""
    assert isinstance(request, HttpRequest)

    context = prepare_general_cxt ()
    context['title'] = 'Delivery Intro.'  

    return render(
        request,
        'app/delivery_intro.html',
        context
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    context = prepare_general_cxt ()
    context['title'] = _('About')
    context['message'] = _('Xiao Bin Cheng Store')
    

    return render(
        request,
        'app/about.html',
        context
    )

def products(request):
    from app.models import Product, ProductCategory
    from math import ceil

    DEF_ITEMS_PER_PAGE = 12

    """Renders the products page."""
    assert isinstance(request, HttpRequest)

    context = prepare_general_cxt ()
    context['title'] = _('Product')

    if request.method == 'GET':
        category = request.GET.get ('c')
        if category and int (category):
            category = "{0:02d}".format (int(category))
        else:
            # default display 01 category
            category = "01"

        context['category'] = ProductCategory.objects.get (code = category)

        items_per_page = request.GET.get ('ipp') or DEF_ITEMS_PER_PAGE
        items_per_page = items_per_page and int(items_per_page) or DEF_ITEMS_PER_PAGE

        page = request.GET.get ('p') or 1
        page = int(page) or 0

        total = request.GET.get ('t')
        total = total and int(total)

        product_search = request.GET.get ('s')
        logger.info ('Search Product with: {}'.format (product_search))

        if category:
            if product_search and len(product_search) > 0:
                logger.info ('Apply product filter with name_indo__iexact: {}'.format (product_search))
                products = Product.objects.filter (name_indo__icontains = product_search, category__code = category).order_by('name_indo')
                context['s'] = product_search
            else:
                products = Product.objects.filter (category__code = category).order_by('name_indo')

            if not total:
                total = products.count ()

            logger.info ('length of products: {}'.format (total))
            context['c'] = category
            context['ipp'] = items_per_page
            context['p'] = page
            context['t'] = total
            context['pt'] = ceil(total/float (items_per_page))    # page total

            logger.info ("c={}, s={}, ipp={}, p={}, t={}, pt={}".format (category,
                                                                            product_search,
                                                                            items_per_page,
                                                                            page,
                                                                            total,
                                                                            ceil(total/float (items_per_page))
                                                                            )
                        )

            limited_product = products[items_per_page*(page-1):items_per_page*(page-1)+items_per_page]

            logger.info ('limited product count = {}'.format (limited_product.count ()))

            context['products'] = limited_product
        else:
            context['ipp'] = items_per_page
            context['p'] = page
            context['t'] = total
            context['pt'] = ceil(total/float (items_per_page))    # page total
            context['products'] = Product.objects.order_by('name_indo').all ()[items_per_page*(page-1):items_per_page*(page-1)+items_per_page]
    return render(
        request,
        'app/products.html',
        context
    )