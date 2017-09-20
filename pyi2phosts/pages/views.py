# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from pyi2phosts.pages.models import Page

class PageView(TemplateView):
    """ Render page with our content """

    template_name = "page.html"

    def get_context_data(self, **kwargs):

        context = super(PageView, self).get_context_data(**kwargs)
        try:
            context['page'] = Page.objects.get(name=context['page_name'])
        except ObjectDoesNotExist:
            self.template_name = "missing_page.html"
        return context
